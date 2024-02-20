from torch.utils.data import Dataset
from torchvision.transforms import ToTensor
import nibabel as nib
import os
import pandas as pd
import numpy as np
import torch

# ADNI中的T1W MRI
class ADNIDataset(Dataset):
    
    # 初始化
    def __init__(self, data_dir, csv_path, transform=None):
        # 读取信息
        self.data_dir = data_dir
        csv = pd.read_csv(csv_path)
        self.data_info = csv.sample(frac=1).reset_index(drop=True)
        self.transform = transform
        self.label_mapping = {'CN': 0, 'MCI': 1, 'AD': 2}
        
        # 删除不存在的数据
        delete_rows = []
        for i in range(len(self.data_info)):
            img_path = os.path.join(self.data_dir, f"brain_adni_{self.data_info.iloc[i, 1][-4:]}_{self.data_info.iloc[i, 0]}_fsld.nii.gz")
            if not os.path.exists(img_path):
                delete_rows.append(i)
        self.data_info = self.data_info.drop(self.data_info.index[delete_rows]).reset_index(drop=True)
        
        self.labels = self.data_info.iloc[:, 2].value_counts().to_dict()
        
    # 获取数据
    def __getitem__(self, index):
        img_path = os.path.join(self.data_dir, f"brain_adni_{self.data_info.iloc[index, 1][-4:]}_{self.data_info.iloc[index, 0]}_fsld.nii.gz")
        label_str = self.data_info.iloc[index, 2]
        nii_img = nib.load(img_path).get_fdata()
        label = self.label_mapping[label_str]
        nii_img = nii_img.astype(np.float32)
        nii_img = torch.from_numpy(nii_img)
        nii_img = nii_img.unsqueeze(0)

        if self.transform is not None:
            nii_img = self.transform(nii_img)
        
        # img结构：[通道, 深度, 高度, 宽度]
        return nii_img, label

    
    # 获取长度
    def __len__(self):
        return len(self.data_info)
    
if __name__ == '__main__':
    dataset = ADNIDataset(data_dir="D:/Data/MRI/ADNI/Image", csv_path="D:/Data/MRI/ADNI/pheno_ADNI_longitudinal_new.csv")
    print('img type:', type(dataset[0][0]), '\nlabel type:', type(dataset[0][1]))
    print('img shape:', dataset[0][0].shape, '\nlabel:', dataset[0][1])
    print(dataset.labels)