import numpy as np
import torch
import os
from monai import transforms

from model import *

class Predictor:
    def __init__(self) -> None:
        self.model_classification = VoxVGG(3)
        self.model_simclr = VoxVGG_SimCLR(256)
        self.model_simclr.backbone.last_fc = torch.nn.Identity()
        self.model_classification = self.load_model_classification(self.model_classification, "./weights/checkpoint_classification_vgg.pth")
        self.model_simclr = self.load_model_simclr(self.model_simclr, "./weights/checkpoint_simclr_vgg.pth")        
        
    
    def load_model_classification(self, model:nn.Module, weights_path):
        if os.path.isfile(weights_path):
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            weights = torch.load(weights_path, map_location=device)
            for key in weights:
                if key != "model":
                    print(f"{key}:{weights[key]}")
            log = model.load_state_dict(weights["model"])
            print(log)
            print("load success!\n")
        else:
            print(f"No file found at: {weights_path}")
        return model
    
    
    def load_model_simclr(self, model:nn.Module, weights_path):
        if os.path.isfile(weights_path):
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            weights = torch.load(weights_path, map_location=device)
            for key in weights:
                if key != "state_dict" and key != "optimizer":
                    print(f"{key}:{weights[key]}")
            state_dict = weights['state_dict']
            

            for k in list(state_dict.keys()):
                if k.startswith('backbone.last_fc'):
                    del state_dict[k]
            print('keys:', list(state_dict.keys()))
            
            log = model.load_state_dict(state_dict, strict=False)
            print(log)
            print("load success!\n")
        else:
            print(f"No file found at: {weights_path}")
        return model
    
        
    
    def extract(self, nii_img:np.ndarray) -> np.ndarray:
        """_summary_

        Args:
            nii_img (np.ndarray): (91 x 109 x 91)

        Returns:
            np.ndarray: (128)
        """
        print(f"image dimension: {nii_img.shape}")
        
        transform = transforms.Compose([
            transforms.Resize(spatial_size=[100, 100, 100]),
            transforms.NormalizeIntensity(nonzero=True, channel_wise=True),
        ])
        nii_img = torch.from_numpy(nii_img)
        nii_img = nii_img.unsqueeze(0)
        nii_img = transform(nii_img)
        nii_img = nii_img.unsqueeze(0)
        nii_img = nii_img.as_tensor()
        self.model_simclr.eval()
        with torch.no_grad():
            # 进行预测
            outputs = self.model_simclr(nii_img)
        outputs = outputs.detach().cpu().numpy()[0]
        return outputs
        
        # random_normal_array = np.random.randn(128)
        # return random_normal_array