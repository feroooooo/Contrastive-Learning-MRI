from torch.utils.data import Dataset
from torchvision.transforms import ToTensor
from torchvision import transforms
import nibabel as nib
import os
import pandas as pd
import numpy as np
import torch

# ADNI中的T1W MRI
class ADNIDataset(Dataset):
    
    # 初始化
    def __init__(self, data_dir, csv_path, transform=None, nomalization=True):
        # 读取信息
        self.data_dir = data_dir
        self.nomalization= nomalization
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
        # if self.nomalization == True:
        #     nii_img = transforms.Normalize((0.1307,), (0.3081,))(nii_img)
        
        # img结构：[通道, 深度, 高度, 宽度] 1 x 91 x 109 x 91
        return nii_img, label

    
    # 获取长度
    def __len__(self):
        return len(self.data_info)
    
if __name__ == '__main__':
    data_dir = "E:/Data/ADNI/adni-fnirt-corrected"
    from monai.transforms import Compose, RandRotate90, RandFlip, NormalizeIntensity, Resize
    transform = Compose([
        NormalizeIntensity(nonzero=True, channel_wise=True),
        RandRotate90(prob=0.5, spatial_axes=[1, 2]),
        RandFlip(prob=0.5, spatial_axis=0),
        # 添加其他变换
        Resize(spatial_size=[91, 109, 91]),
    ])
    dataset = dataset = ADNIDataset(data_dir=data_dir, csv_path="E:/Data/ADNI/train label.csv", transform=transform)
    print('img type:', type(dataset[0][0]), '\nlabel type:', type(dataset[0][1]))
    print('img shape:', dataset[0][0].shape, '\nlabel:', dataset[0][1])
    print(dataset.labels)
    print(dataset.data_info.iloc[0])
    # print(dataset[0][0][0][45][45])
    # for i in range(50, dataset[0][0][0].shape[0]):
    #     for j in range(dataset[0][0][0].shape[1]):
    #         for k in range(dataset[0][0][0].shape[2]):
    #             print(dataset[0][0][0][i][j][k].item(), i, j, k)