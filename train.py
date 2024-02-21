import torch.optim as optim
import torch
import torch.nn as nn
import os
import time
from torch.utils.data import DataLoader, random_split
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter
from mri_dataset import ADNIDataset
from model import Simple3DCNN

# TensorBoard
path = 'logs'
if os.path.exists('logs'):
    for file_name in os.listdir(path):
        os.remove(os.path.join(path, file_name))
writer = SummaryWriter("logs")

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
        if batch_idx % 100 == 0:
            print(f'\rEpoch: {epoch}\t{batch_idx * len(data):>4} / {len(train_loader.dataset):<4} ({100. * batch_idx / len(train_loader):.0f}%)\tLoss: {loss.item():.6f}', end='')
        if step % 100 == 0:
            writer.add_scalar("train loss", loss.item(), step)
        step += 1
    print(f'\rEpoch: {epoch}\t{len(train_loader.dataset):>4} / {len(train_loader.dataset):<4} ({100.:.0f}%)\tLatest Loss: {loss.item():.6f}')


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
        for data, target in validation_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            validation_loss += criterion(output, target).item() * data.size(0)
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()
    validation_loss /= len(validation_loader.dataset)

    accuracy = correct / len(validation_loader.dataset)
    print('Validate:\tAverage Loss: {:.4f}\tAccuracy: {}/{} ({:.1f}%)\n'.format(
        validation_loss, correct, len(validation_loader.dataset), accuracy * 100.))
    writer.add_scalar("validation loss", validation_loss, epoch)
    writer.add_scalar("validation accuracy", accuracy, epoch)
    
    # 存储模型
    global best_accuracy
    global best_loss
    if best_accuracy < accuracy:
        best_accuracy = accuracy
        print('Saving model...')
        state = {
            'model': model.state_dict(),
            'accuracy': accuracy,
            'loss': validation_loss,
            'epoch': epoch,
        }
        if not os.path.isdir('checkpoint'):
            os.mkdir('checkpoint')
        torch.save(state, 'checkpoint/best.pth')
    if best_loss > validation_loss:
        best_loss = validation_loss
        
        
# 测试
def test(model, device, test_loader, criterion):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += criterion(output, target).item() * data.size(0)
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()
    test_loss /= len(test_loader.dataset)

    accuracy = correct / len(test_loader.dataset)
    print('Test:\tAverage Loss: {:.4f}\tAccuracy: {}/{} ({:.1f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset), accuracy * 100.))


# 向控制台打印蓝色字符串
def color_print(str):
    print(f"\033[94m{str}\033[0m")


# 超参数配置
epoch_num = 30
batch_size = 8
learning_rate = 0.0001

if __name__ == "__main__":
    time_start = time.perf_counter()
    color_print("Infomations:")
    # 初始化数据集
    data_dir = "D:/Data/MRI/ADNI/Image"
    csv_path = "D:/Data/MRI/ADNI/pheno_ADNI_longitudinal_new.csv"
    
    transform = transforms.Normalize((0.1307,), (0.3081,))
    dataset = ADNIDataset(data_dir=data_dir, csv_path=csv_path, transform=transform)

    # 数据集大小
    dataset_size = len(dataset)
    train_size = int(dataset_size * 0.7)
    validation_size = int(dataset_size * 0.15)
    test_size = dataset_size - train_size - validation_size
    print("train size:", train_size)
    print("validation size:", validation_size)
    print("test size:", test_size)

    # 数据集切分
    train_dataset, validation_dataset, test_dataset = random_split(dataset, [train_size, validation_size, test_size])

    # DataLoader
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    validation_loader = DataLoader(validation_dataset, batch_size=batch_size, shuffle=False)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print('current device:', device)
    # 实例化网络
    model = Simple3DCNN().to(device)
    # 定义损失函数和优化器
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    
    color_print("\nStart Training:")
    for epoch in range(1, epoch_num + 1):  # 总共训练2个epochs
        train(model, device, train_loader, optimizer, criterion, epoch)
        validate(model, device, validation_loader, criterion)
    
    writer.close()
    time_stop = time.perf_counter()
    color_print("Finish Training.")
    
    print(f"\ntotal time:{time_stop - time_start:.3f}s")
    print(f"best loss: {best_loss:.6f}")
    print(f"best accuracy: {best_accuracy * 100.:.1f}%\n")
    
    test(model, device, test_loader, criterion)
