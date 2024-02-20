from torch.utils.data import Dataset
from PIL import Image
import pandas as pd
import os

class ImageDataset(Dataset):
    
    def __init__(self, data_dir, transform=None, train=True):
        self.data_dir = data_dir
        if train:
            self.dataset_type = "train"
        else:
            self.dataset_type = "test"
        label = pd.read_csv(os.path.join(data_dir, f"{self.dataset_type}_label.csv"))
        self.data_info = label.sample(frac=1).reset_index(drop=True)
        self.label_names = self.data_info['label'].unique().tolist()
        self.transform = transform

        
    def __getitem__(self, index):
        img_path = os.path.join(self.data_dir, self.dataset_type, self.data_info.iloc[index, 0])
        label = self.data_info.iloc[index, 1]
        img = Image.open(img_path).convert('RGB')     

        if self.transform is not None:
            img = self.transform(img)
 
        return img, label

    
    def __len__(self):
        return len(self.data_info)
    

