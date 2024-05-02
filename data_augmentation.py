from monai.transforms import *
import numpy as np

class MRIAugmentation:
    def __init__(self) -> None:
        pass
    
    def get_pre_transforms(size=100):
        pre_transforms = Compose([
            Resize(spatial_size=[size, size, size]),
            NormalizeIntensity(channel_wise=True),
        ])
        return pre_transforms
    
    
    def get_augmentation_transforms(size=100):
        transform = Compose([
            # 随机裁剪
            RandSpatialCrop(roi_size=(81, 99, 81), random_size=True),
            
            # 翻转和旋转
            RandFlip(prob=0.5, spatial_axis=0),
            
            
            # RandRotate90(prob=0.5, spatial_axes=[1, 2]),
            # RandRotate90(prob=0.5, spatial_axes=[0, 1]),
            # RandRotate90(prob=0.5, spatial_axes=[0, 2]),
            # RandFlip(prob=0.5, spatial_axis=1),
            # RandFlip(prob=0.5, spatial_axis=2),
            
            
            RandRotate(range_x=(-15, 15), range_y=(-15, 15), range_z=(-15, 15), prob=0.5),
            
            # 随机对比度
            RandAdjustContrast(prob=0.7, gamma=(0.5, 1.5)),
            # 随机高斯噪声
            RandGaussianNoise(prob=0.5),
            # 随机仿射变换
            RandAffine(prob=0.7, translate_range=10, scale_range=(0.9, 1.1), rotate_range=(0, 0, np.pi/15)),
            
            Resize(spatial_size=[size, size, size]),
            NormalizeIntensity(channel_wise=True),
        ])
        return transform
    