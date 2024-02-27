import torch
from torch.utils.data import DataLoader, WeightedRandomSampler
from mri_dataset import ADNIDataset
from torchvision import transforms

transform = transforms.Normalize((0.1307,), (0.3081,))
data_dir = "C:/Custom/DataSet/ADNI_预处理后/Image"
train_dataset = ADNIDataset(data_dir=data_dir, csv_path="C:/Custom/DataSet/ADNI_预处理后/train label.csv", transform=transform)

all_labels = []
for _, label in train_dataset:
    all_labels.append(label)
all_labels = torch.tensor(all_labels)
class_count = torch.tensor([(all_labels == t).sum() for t in torch.unique(all_labels, sorted=True)])

class_weights = 1. / class_count.float()  # 计算类权重
samples_weights = class_weights[all_labels.long()]  # 每个样本的权重
sampler = WeightedRandomSampler(weights=samples_weights, num_samples=len(samples_weights), replacement=True)

print(class_count)
print(class_weights)
print(samples_weights.shape)



# 假设有一个带有标签的数据集
# labels = [0, 1, 1, 1, 1, 1, 0, 1, 0, 1]  # 示例标签
# class_count = torch.tensor([labels.count(0), labels.count(1)])  # 计算每个类的数量
# class_weights = 1. / class_count  # 计算类权重
# samples_weights = class_weights[labels]  # 每个样本的权重
# sampler = WeightedRandomSampler(weights=samples_weights, num_samples=len(samples_weights), replacement=True)

# print(class_count)
# print(class_weights)
# print(samples_weights.shape)

# 使用WeightedRandomSampler创建DataLoader
# data_loader = DataLoader(train_dataset, batch_size=2, sampler=sampler)