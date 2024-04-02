import torch
from torch.utils.data import DataLoader
import torch.nn as nn
from sklearn.metrics import balanced_accuracy_score, precision_recall_fscore_support, confusion_matrix

from mri_dataset import ADNIDataset
from model import VoxVGG
from data_augmentation import MRIAugmentation

args = {}
args['arch'] = 'vgg'
args['weight_path'] = './weights/checkpoint_classification_vgg.pth'
# args['weight_path']= './runs/simclr_fintune_vgg/checkpoint_best.pth'
args['data_dir'] = "E:/Data/ADNI/adni-fnirt-corrected"
args['csv_train_path'] = "E:/Data/ADNI/single_train.csv"
args['csv_validation_path'] = "E:/Data/ADNI/single_validation.csv"
args['csv_test_path'] = "E:/Data/ADNI/single_test.csv"
args['batch_size'] = 8

pre_transform = MRIAugmentation.get_pre_transforms()

test_dataset = ADNIDataset(data_dir=args['data_dir'], csv_path=args['csv_test_path'], transform=pre_transform)
print(test_dataset.labels)
loader = DataLoader(test_dataset, batch_size=args['batch_size'], shuffle=False)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

weights = torch.load(args['weight_path'], map_location=device)

model = VoxVGG(class_nums=3).to(device)
model.load_state_dict(weights["model"], strict=False)
criterion = nn.CrossEntropyLoss().to(device)

model.eval()

# 初始化存储预测和真实标签的列表
all_preds = []
all_targets = []

with torch.no_grad():
    for idx, (data, target) in enumerate(loader):
        print(f"\r{idx + 1}/ {len(loader)}", end="")
        data, target = data.to(device), target.to(device)
        output = model(data)

        # 获取最大概率的预测结果
        pred = output.argmax(dim=1)
        
        # 保存预测和目标值，以便后续计算指标
        all_preds.extend(pred.view(-1).cpu().numpy())
        all_targets.extend(target.view(-1).cpu().numpy())
    print("")
    
# 计算平衡准确率
balanced_acc = balanced_accuracy_score(all_targets, all_preds)

# 计算宏精确率、宏召回率和宏F1分数
precision, recall, f1, _ = precision_recall_fscore_support(all_targets, all_preds, average='macro')

# 计算混淆矩阵
conf_matrix = confusion_matrix(all_targets, all_preds)

# 打印结果
print(f"平衡准确率: {balanced_acc}")
print(f"宏精确率: {precision}")
print(f"宏召回率: {recall}")
print(f"宏F1分数: {f1}")
print("混淆矩阵:")
print(conf_matrix)