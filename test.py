from torchvision import transforms
from mri_dataset import ADNIDataset
transform = transforms.Normalize((0.1307,), (0.3081,))
train_dataset = ADNIDataset(data_dir="E:/Data/ADNI/adni-fnirt-corrected", csv_path="E:/Data/ADNI/train label.csv", transform=transform)
validation_dataset = ADNIDataset(data_dir="E:/Data/ADNI/adni-fnirt-corrected", csv_path="E:/Data/ADNI/validation label.csv", transform=transform)
test_dataset = ADNIDataset(data_dir="E:/Data/ADNI/adni-fnirt-corrected", csv_path="E:/Data/ADNI/test label.csv", transform=transform)

print("train size:", len(train_dataset))
print("validation size:", len(validation_dataset))
print("test size:", len(test_dataset))
print("total size:", len(train_dataset) + len(validation_dataset) + len(test_dataset))