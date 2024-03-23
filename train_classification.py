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

# TensorBoard
writer = SummaryWriter()

logging.basicConfig(filename=os.path.join(writer.log_dir, 'training.log'), level=logging.INFO)


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
    logging.info('Validate:\tAverage Loss: {:.4f}\tAccuracy: {}/{} ({:.1f}%)'.format(validation_loss, correct, len(validation_loader.dataset), accuracy * 100.))
    
    # 存储模型
    global best_accuracy
    global best_loss
    if best_accuracy < accuracy:
        best_accuracy = accuracy
        print('Saving model...\n')
        state = {
            'model': model.state_dict(),
            'accuracy': accuracy,
            'loss': validation_loss,
            'epoch': epoch,
        }
        # if not os.path.isdir('checkpoint'):
        #     os.mkdir('checkpoint')
        torch.save(state, os.path.join(writer.log_dir, 'checkpoint_best.pth'))
    if best_loss > validation_loss:
        best_loss = validation_loss
        
        
# # 测试
# def test(model, device, test_loader, criterion):
#     model.eval()
#     test_loss = 0
#     correct = 0
#     with torch.no_grad():
#         for data, target in test_loader:
#             data, target = data.to(device), target.to(device)
#             output = model(data)
#             test_loss += criterion(output, target).item() * data.size(0)
#             pred = output.argmax(dim=1, keepdim=True)
#             correct += pred.eq(target.view_as(pred)).sum().item()
#     test_loss /= len(test_loader.dataset)

#     accuracy = correct / len(test_loader.dataset)
#     print('Test:\tAverage Loss: {:.4f}\tAccuracy: {}/{} ({:.1f}%)\n'.format(
#         test_loss, correct, len(test_loader.dataset), accuracy * 100.))
    
    
# # 评估测试集
# def train_eval(model, device, train_loader, criterion):
#     test_loader = train_loader
#     model.eval()
#     test_loss = 0
#     correct = 0
#     with torch.no_grad():
#         for data, target in test_loader:
#             data, target = data.to(device), target.to(device)
#             output = model(data)
#             test_loss += criterion(output, target).item() * data.size(0)
#             pred = output.argmax(dim=1, keepdim=True)
#             correct += pred.eq(target.view_as(pred)).sum().item()
#     test_loss /= len(test_loader.dataset)

#     accuracy = correct / len(test_loader.dataset)
#     print('Train:\tAverage Loss: {:.4f}\tAccuracy: {}/{} ({:.1f}%)\n'.format(
#         test_loss, correct, len(test_loader.dataset), accuracy * 100.))
    

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


# 超参数配置
args = {}
epoch_num = 50
batch_size = 8
learning_rate = 0.0001
data_type = 'single'
args['model'] = 'simple'

if __name__ == "__main__":
    time_start = time.perf_counter()
    color_print("Infomations:")
    # 初始化数据集
    data_dir = "E:/Data/ADNI/adni-fnirt-corrected"
    
    
    size = 100
    # 数据增强
    from monai.transforms import Compose, RandRotate90, RandFlip, NormalizeIntensity, Resize, RandAdjustContrast, RandGaussianNoise, RandAffine
    prob = 0.5
    transform = Compose([
        RandRotate90(prob=prob, spatial_axes=[1, 2]),
        # RandRotate90(prob=prob, spatial_axes=[0, 1]),
        # RandRotate90(prob=prob, spatial_axes=[0, 2]),
        RandFlip(prob=prob, spatial_axis=0),
        # RandFlip(prob=prob, spatial_axis=1),
        # RandFlip(prob=prob, spatial_axis=2),
        
        RandAdjustContrast(prob=prob, gamma=(0.7, 1.3)),
        RandGaussianNoise(prob=prob),
        # RandAffine(prob=prob, translate_range=10, scale_range=(0.9, 1.1), rotate_range=45),
        
        Resize(spatial_size=[size, size, size]),
        NormalizeIntensity(channel_wise=True),
    ])
    
    pre_transform = Compose([
        Resize(spatial_size=[size, size, size]),
        NormalizeIntensity(channel_wise=True),
    ])
    
    # 导入数据集
    # 先导入数据，再切分
    if data_type == 'all' or 'single':
        # 全部数据，不针对被试分割数据集，存在信息泄露
        if data_type == 'all':
            csv_path = r"E:/Data/ADNI/pheno_ADNI_longitudinal_new.csv"
        elif data_type == 'single':
            csv_path = r"E:\Data\ADNI\single_subject.csv"
        
        dataset = ADNIDataset(data_dir=data_dir, csv_path=csv_path, transform=transform)
        # 数据集大小
        dataset_size = len(dataset)
        train_size = int(dataset_size * 0.7)
        validation_size = int(dataset_size * 0.15)
        test_size = dataset_size - train_size - validation_size

        # 数据集切分
        train_dataset, validation_dataset, test_dataset = random_split(dataset, [train_size, validation_size, test_size])
        
    # 提取分割的数据集，每个被试只存在于一个集合
    elif data_type == 'split':
        train_dataset = ADNIDataset(data_dir=data_dir, csv_path="E:/Data/ADNI/train label.csv", transform=transform)
        validation_dataset = ADNIDataset(data_dir=data_dir, csv_path="E:/Data/ADNI/validation label.csv", transform=pre_transform)
        test_dataset = ADNIDataset(data_dir=data_dir, csv_path="E:/Data/ADNI/test label.csv", transform=pre_transform)

    print("train size:", len(train_dataset))
    # print(train_dataset.labels)
    print("validation size:", len(validation_dataset))
    # print(validation_dataset.labels)
    print("test size:", len(test_dataset))
    # print(test_dataset.labels)
    print("total size:", len(train_dataset) + len(validation_dataset) + len(test_dataset))
    # 数据集导入完成
    
    
    # 是否使用采样器
    use_sampler = False
    
    if use_sampler:
        # 类别不平衡
        all_labels = []
        for _, label in train_dataset:
            all_labels.append(label)
        all_labels = torch.tensor(all_labels)
        class_count = torch.tensor([(all_labels == t).sum() for t in torch.unique(all_labels, sorted=True)])

        class_weights = 1. / class_count.float()  # 计算类权重
        samples_weights = class_weights[all_labels.long()]  # 每个样本的权重
        sampler = WeightedRandomSampler(weights=samples_weights, num_samples=len(samples_weights), replacement=True)
        
        train_loader = DataLoader(train_dataset, batch_size=batch_size, sampler=sampler)
    else:
        train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    
    validation_loader = DataLoader(validation_dataset, batch_size=batch_size, shuffle=False)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
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
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)
    
    color_print("\nStart Training:")
    logging.info("Start Training:")
    for epoch in range(1, epoch_num + 1):
        train(model, device, train_loader, optimizer, criterion, epoch)
        eval(model, device, train_loader, criterion, train=True)
        validate(model, device, validation_loader, criterion)
        if epoch > 50:
            scheduler.step()
    
    writer.close()
    time_stop = time.perf_counter()
    color_print("Finish Training.")
    
    print(f"\ntotal time:{time_stop - time_start:.3f}s")
    print(f"best loss: {best_loss:.6f}")
    print(f"best accuracy: {best_accuracy * 100.:.1f}%\n")
    
    eval(model, device, test_loader, criterion, train=False)
