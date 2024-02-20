import torch.optim as optim
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split
from torchvision import transforms
from mri_dataset import ADNIDataset
from model import Simple3DCNN

def train(model, device, train_loader, optimizer, criterion, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 100 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))

def test(model, device, test_loader, criterion):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += criterion(output, target).item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()
    test_loss /= len(test_loader.dataset)

    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


if __name__ == "__main__":
    # 初始化数据集
    data_dir = "D:/Data/MRI/ADNI/Image"
    csv_path = "D:/Data/MRI/ADNI/pheno_ADNI_longitudinal_new.csv"
    
    transform = transforms.Normalize((0.1307,), (0.3081,))
    dataset = ADNIDataset(data_dir=data_dir, csv_path=csv_path, transform=transform)

    # 数据集大小
    dataset_size = len(dataset)
    train_size = int(dataset_size * 0.85)
    test_size = dataset_size - train_size

    # 数据集切分
    train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

    # DataLoader
    batch_size = 4
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # 实例化网络
    model = Simple3DCNN().to(device)
    # 定义损失函数和优化器
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.0001)

    for epoch in range(1, 3):  # 总共训练2个epochs
        train(model, device, train_loader, optimizer, criterion, epoch)
        test(model, device, test_loader, nn.CrossEntropyLoss(reduction='sum'))
