import torch.optim as optim
import torch
import torch.nn as nn
import os
import time
from torch.utils.data import DataLoader, random_split, WeightedRandomSampler
from torch.utils.tensorboard import SummaryWriter
import logging
from mri_dataset import ADNIDataset
from model import Simple3DCNN, VoxVGG, VoxResNet
import yaml

# TensorBoard
writer = SummaryWriter()

logging.basicConfig(filename=os.path.join(writer.log_dir, 'training.log'), level=logging.INFO)


# 超参数以及其它配置信息
args = {}
args['model'] = 'vgg'
args['epoch_num'] = 100
args['batch_size'] = 16
args['learning_rate'] = 0.0001
# 数据形式（single：每个被试图像唯一、split：每个被试图像不唯一，但对于某个被试，其图像只同时存在于一个集合、all：每个被试图像不唯一）
args['data_type'] = 'single'
# 每个数据增强方法的概率
args['prob'] = 1
# 图像resize后的大小，三个维度相同
args['size'] = 100
# 数据路径
args['data_dir'] = "E:/Data/ADNI/adni-fnirt-corrected"
# 是否使用采样器
args['use_sampler'] = True
args['use_cuda'] = True

device = torch.device("cuda" if torch.cuda.is_available() and args['use_cuda'] else "cpu")
if str(device) == "cuda":
    args['use_cuda'] = True
else:
    args['use_cuda'] = False

# 存储信息
with open(os.path.join(writer.log_dir, 'config.yaml'), 'w') as outfile:
    yaml.dump(args, outfile)


# 训练步数
step = 0
# 训练
def train(model, device, train_loader, optimizer, criterion, epoch):
    model.train()
    global step
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        print(f'\rEpoch: {epoch}\t{batch_idx * len(data):>4} / {len(train_loader.dataset):<4} ({100. * batch_idx / len(train_loader):.0f}%)\tLoss: {loss.item():.6f}', end='')
        if step % 100 == 0:
            writer.add_scalar("train loss", loss.item(), step)
        step += 1
    print(f'\rEpoch: {epoch}\t{len(train_loader.dataset):>4} / {len(train_loader.dataset):<4} ({100.:.0f}%)\tLatest Loss: {loss.item():.6f}')
    logging.info(f"Epoch:{epoch}")

# 最优损失函数
best_loss = float("inf")
# 最优准确率
best_accuracy = 0
# 最优时的轮数
best_epoch = 0

# 验证
def validate(model, device, validation_loader, criterion):
    model.eval()
    validation_loss = 0
    correct = 0
    with torch.no_grad():
        for idx, (data, target) in enumerate(validation_loader):
            print(f'\r{idx + 1}/{len(validation_loader)}', end='')
            data, target = data.to(device), target.to(device)
            output = model(data)
            validation_loss += criterion(output, target).item() * data.size(0)
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()
        print('\r', end='')
    validation_loss /= len(validation_loader.dataset)

    accuracy = correct / len(validation_loader.dataset)
    print('Validate:\tAverage Loss: {:.4f}\tAccuracy: {}/{} ({:.1f}%)'.format(validation_loss, correct, len(validation_loader.dataset), accuracy * 100.))
    writer.add_scalar("validation loss", validation_loss, epoch)
    writer.add_scalar("validation accuracy", accuracy, epoch)
    logging.info('Validate:\tAverage Loss: {:.4f}\tAccuracy: {}/{} ({:.1f}%)\n'.format(validation_loss, correct, len(validation_loader.dataset), accuracy * 100.))
    
    # 存储模型
    global best_accuracy
    global best_loss
    global best_epoch
    if best_accuracy < accuracy:
        best_accuracy = accuracy
        best_epoch = epoch
        print('Saving model...\n')
        state = {
            'model': model.state_dict(),
            'accuracy': accuracy,
            'loss': validation_loss,
            'epoch': epoch,
        }
        torch.save(state, os.path.join(writer.log_dir, 'checkpoint_best.pth'))
    if best_loss > validation_loss:
        best_loss = validation_loss
    

# 评估模型
def eval(model, device, loader, criterion, train=True):
    model.eval()
    loss = 0
    correct = 0
    with torch.no_grad():
        for idx, (data, target) in enumerate(loader):
            print(f'\r{idx + 1}/{len(loader)}', end='')
            data, target = data.to(device), target.to(device)
            output = model(data)
            loss += criterion(output, target).item() * data.size(0)
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()
        print('\r', end='')
    loss /= len(loader.dataset)

    accuracy = correct / len(loader.dataset)
    if train:
        print('Train:\tAverage Loss: {:.4f}\tAccuracy: {}/{} ({:.1f}%)'.format(loss, correct, len(loader.dataset), accuracy * 100.))
        writer.add_scalar("average train loss", loss, epoch)
        writer.add_scalar("average train accuracy", accuracy, epoch)
        logging.info('Train:\tAverage Loss: {:.4f}\tAccuracy: {}/{} ({:.1f}%)'.format(loss, correct, len(loader.dataset), accuracy * 100.))
    else:
        print('Test:\tAverage Loss: {:.4f}\tAccuracy: {}/{} ({:.1f}%)'.format(loss, correct, len(loader.dataset), accuracy * 100.))
        logging.info('Test:\tAverage Loss: {:.4f}\tAccuracy: {}/{} ({:.1f}%)'.format(loss, correct, len(loader.dataset), accuracy * 100.))
        print('Saving model...\n')
        state = {
            'model': model.state_dict(),
            'accuracy': accuracy,
            'loss': loss,
            'epoch': epoch,
        }
        torch.save(state, os.path.join(writer.log_dir, 'checkpoint_last.pth'))


# 向控制台打印蓝色字符串
def color_print(str):
    print(f"\033[94m{str}\033[0m")


if __name__ == "__main__":
    time_start = time.perf_counter()
    color_print("Infomations:")
    # 初始化数据集
    # 数据增强
    from monai.transforms import Compose, RandRotate90, RandFlip, NormalizeIntensity, Resize, RandAdjustContrast, RandGaussianNoise, RandAffine
    
    transform = Compose([
        RandRotate90(prob=0.5, spatial_axes=[1, 2]),
        RandRotate90(prob=0.5, spatial_axes=[0, 1]),
        RandRotate90(prob=0.5, spatial_axes=[0, 2]),
        RandFlip(prob=0.5, spatial_axis=0),
        RandFlip(prob=0.5, spatial_axis=1),
        RandFlip(prob=0.5, spatial_axis=2),
        
        RandAdjustContrast(prob=args['prob'], gamma=(0.5, 1.5)),
        RandGaussianNoise(prob=args['prob']),
        # RandAffine(prob=args['prob'], translate_range=10, scale_range=(0.9, 1.1), rotate_range=45),
        
        Resize(spatial_size=[args['size'], args['size'], args['size']]),
        NormalizeIntensity(channel_wise=True),
    ])
    
    pre_transform = Compose([
        Resize(spatial_size=[args['size'], args['size'], args['size']]),
        NormalizeIntensity(channel_wise=True),
    ])
    
    # 导入数据集
    # 先导入数据，再切分
    if args['data_type'] == 'all' or 'single':
        # 全部数据，不针对被试分割数据集，存在信息泄露
        if args['data_type'] == 'all':
            csv_path = r"E:/Data/ADNI/pheno_ADNI_longitudinal_new.csv"
        elif args['data_type'] == 'single':
            csv_path = r"E:\Data\ADNI\single_subject.csv"
        
        dataset = ADNIDataset(data_dir=args['data_dir'], csv_path=csv_path, transform=transform)
        # 数据集大小
        dataset_size = len(dataset)
        train_size = int(dataset_size * 0.7)
        validation_size = int(dataset_size * 0.15)
        test_size = dataset_size - train_size - validation_size

        # 数据集切分
        train_dataset, validation_dataset, test_dataset = random_split(dataset, [train_size, validation_size, test_size])
        validation_dataset.transform = test_dataset.transform = pre_transform
        
    # 提取分割的数据集，每个被试只存在于一个集合
    elif args['data_type'] == 'split':
        train_dataset = ADNIDataset(data_dir=args['data_dir'], csv_path="E:/Data/ADNI/train label.csv", transform=transform)
        validation_dataset = ADNIDataset(data_dir=args['data_dir'], csv_path="E:/Data/ADNI/validation label.csv", transform=pre_transform)
        test_dataset = ADNIDataset(data_dir=args['data_dir'], csv_path="E:/Data/ADNI/test label.csv", transform=pre_transform)
    import copy
    train_eval_dataset = copy.deepcopy(train_dataset)
    train_eval_dataset.transform = pre_transform

    train_size = len(train_dataset)
    validation_size = len(validation_dataset)
    test_size = len(test_dataset)
    total_size = len(train_dataset) + len(validation_dataset) + len(test_dataset)
    logging.info(f"train size:{train_size}")
    logging.info(f"validation size:{validation_size}")
    logging.info(f"test size:{test_size}")
    logging.info(f"total size:{total_size}\n")
    print(f"train size:{train_size}")
    # print(train_dataset.labels)
    print(f"validation size:{validation_size}")
    # print(validation_dataset.labels)
    print(f"test size:{test_size}")
    # print(test_dataset.labels)
    print(f"total size:{total_size}\n")
    # 数据集导入完成
    
    
    if args['use_sampler']:
        # 类别不平衡
        all_labels = []
        for _, label in train_dataset:
            all_labels.append(label)
        all_labels = torch.tensor(all_labels)
        class_count = torch.tensor([(all_labels == t).sum() for t in torch.unique(all_labels, sorted=True)])

        class_weights = 1. / class_count.float()  # 计算类权重
        samples_weights = class_weights[all_labels.long()]  # 每个样本的权重
        sampler = WeightedRandomSampler(weights=samples_weights, num_samples=len(samples_weights), replacement=True)
        
        train_loader = DataLoader(train_dataset, batch_size=args['batch_size'], sampler=sampler)
    else:
        train_loader = DataLoader(train_dataset, batch_size=args['batch_size'], shuffle=True)
    
    train_eval_loader = DataLoader(train_eval_dataset, batch_size=args['batch_size'], shuffle=False)
    validation_loader = DataLoader(validation_dataset, batch_size=args['batch_size'], shuffle=False)
    test_loader = DataLoader(test_dataset, batch_size=args['batch_size'], shuffle=False)
    
    print('current device:', device)
    # 实例化网络
    if args['model'] == 'simple':
        model = Simple3DCNN(class_nums=3).to(device)
    elif args['model'] == 'vgg':
        model = VoxVGG(class_nums=3).to(device)
    elif args['model'] == 'resnet':
        model = VoxResNet(class_nums=3).to(device)
    # 定义损失函数和优化器
    criterion = nn.CrossEntropyLoss().to(device)
    optimizer = optim.Adam(model.parameters(), lr=args['learning_rate'])
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)
    
    color_print("\nStart Training:")
    logging.info("Start Training:\n")
    for epoch in range(1, args['epoch_num'] + 1):
        train(model, device, train_loader, optimizer, criterion, epoch)
        eval(model, device, train_eval_loader, criterion, train=True)
        validate(model, device, validation_loader, criterion)
        if epoch > 50:
            scheduler.step()
    
    writer.close()
    time_stop = time.perf_counter()
    color_print("Finish Training.")
    
    logging.info(f"total time:{time_stop - time_start:.3f}s")
    logging.info(f"best loss: {best_loss:.6f}")
    logging.info(f"best accuracy: {best_accuracy * 100.:.1f}%")
    logging.info(f"best epoch: {best_epoch}\n")
    print(f"\ntotal time:{time_stop - time_start:.3f}s")
    print(f"best loss: {best_loss:.6f}")
    print(f"best accuracy: {best_accuracy * 100.:.1f}%")
    print(f"best epoch: {best_epoch}\n")
    
    eval(model, device, test_loader, criterion, train=False)
