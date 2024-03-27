import numpy as np
import torch
import os
from medcam import medcam
from monai import transforms

from model import *

class Predictor:
    def __init__(self) -> None:
        self.model_classification = VoxVGG(3)
        self.model_classification = medcam.inject(self.model_classification, output_dir='attention_maps', backend='gcam', save_maps=False, return_attention=True, layer='auto')
        self.model_simclr = VoxVGG_SimCLR(256)
        self.model_simclr.backbone.last_fc = torch.nn.Identity()
        # self.model_classification = self.load_model_classification(self.model_classification, "./weights/checkpoint_classification_vgg.pth")
        # self.model_simclr = self.load_model_simclr(self.model_simclr, "./weights/checkpoint_simclr_vgg.pth")        
        
    
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
        nii_img = self.img_pre_process(nii_img)
        self.model_simclr.eval()
        with torch.no_grad():
            # 进行预测
            outputs = self.model_simclr(nii_img)
        outputs = outputs.detach().cpu().numpy()[0]
        return outputs
        
        # random_normal_array = np.random.randn(128)
        # return random_normal_array
    
        
    def classify(self, nii_img:np.ndarray):
        nii_img = self.img_pre_process(nii_img)
        label_mapping = {0: 'CN', 1: 'MCI', 2: 'AD'}
        self.model_classification.eval()
        with torch.no_grad():
            outputs, attention_map = self.model_classification(nii_img)
            print(outputs)
            _, pred = torch.max(outputs, 1)
            attention_map = np.squeeze(attention_map.detach().cpu().numpy())
            # 返回Predicted class
        print(label_mapping[pred.item()])
        print("attention map shape:", attention_map.shape)
        return label_mapping[pred.item()], attention_map
    
    
    def img_pre_process(self, nii_img):
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
        return nii_img