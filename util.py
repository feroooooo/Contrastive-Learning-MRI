import numpy as np
import math
from matplotlib import colormaps
from scipy.ndimage import zoom

from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap

class Util:
    @staticmethod
    def normalize_image_0_to_1(image: np.ndarray) -> np.ndarray:
        """
        将输入的三维图像归一化到0-1范围。
        param image: 三维Numpy数组，代表图像数据。
        return: 归一化后的图像数据。
        """
        # 计算图像的最小值和最大值
        min_val = np.min(image)
        max_val = np.max(image)
        
        if min_val == max_val:
            return image
        
        # 应用最大-最小归一化
        normalized_image = (image - min_val) / (max_val - min_val)
        
        return normalized_image
    
    
    @staticmethod
    def img_from_0_1_to_0_255(npImage: np.ndarray) -> np.ndarray:
        return (npImage * 255).astype(np.uint8)
    
    @staticmethod
    def from_3d_img_get_central_xyz(nii_img):
        x = math.floor(nii_img.shape[0] / 2)
        y = math.floor(nii_img.shape[1] / 2)
        z = math.floor(nii_img.shape[2] / 2)
        return x, y, z
    
    
    @staticmethod
    def from_3d_img_get_pixmap(nii_img, x, y, z):
        nii_img = nii_img
        nii_img = Util.img_from_0_1_to_0_255(Util.normalize_image_0_to_1(nii_img))

        saggital_img = np.rot90(nii_img[x, :, :][:, ::-1], k=-1)
        saggital_img = np.ascontiguousarray(saggital_img)
        
        coronal_img = np.flipud(nii_img[:, y, :].T)
        coronal_img = np.ascontiguousarray(coronal_img)
        
        axial_img = np.flipud(nii_img[:, :, z].T)
        axial_img = np.ascontiguousarray(axial_img)

        targetWidth = 250
        targetHeight = 250
        
        h, w = saggital_img.shape
        saggital_pixmap = QPixmap.fromImage(QImage(saggital_img.data, w, h, w, QImage.Format_Grayscale8)).scaled(targetWidth, targetHeight, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        h, w = coronal_img.shape
        coronal_pixmap = QPixmap.fromImage(QImage(coronal_img.data, w, h, w, QImage.Format_Grayscale8)).scaled(targetWidth, targetHeight, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        h, w = axial_img.shape
        axial_pixmap = QPixmap.fromImage(QImage(axial_img.data, w, h, w, QImage.Format_Grayscale8)).scaled(targetWidth, targetHeight, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        
        return saggital_pixmap, coronal_pixmap, axial_pixmap
    
    
    @staticmethod
    def from_3d_rgb_img_get_pixmap(nii_img, x, y, z):
        nii_img = nii_img
        nii_img = Util.img_from_0_1_to_0_255(Util.normalize_image_0_to_1(nii_img))

        saggital_img = np.rot90(nii_img[x, :, :, :][:, ::-1, :], k=-1)
        saggital_img = np.ascontiguousarray(saggital_img)
        
        coronal_img = np.flipud(np.transpose(nii_img[:, y, :, :], (1, 0, 2)))
        coronal_img = np.ascontiguousarray(coronal_img)
        
        axial_img =  np.flipud(np.transpose(nii_img[:, :, z, :], (1, 0, 2)))
        axial_img = np.ascontiguousarray(axial_img)

        targetWidth = 250
        targetHeight = 250
        
        h, w, c = saggital_img.shape
        saggital_pixmap = QPixmap.fromImage(QImage(saggital_img.data, w, h, c * w, QImage.Format_RGB888)).scaled(targetWidth, targetHeight, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        h, w, c = coronal_img.shape
        coronal_pixmap = QPixmap.fromImage(QImage(coronal_img.data, w, h, c * w, QImage.Format_RGB888)).scaled(targetWidth, targetHeight, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        h, w, c = axial_img.shape
        axial_pixmap = QPixmap.fromImage(QImage(axial_img.data, w, h, c * w, QImage.Format_RGB888)).scaled(targetWidth, targetHeight, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        
        return saggital_pixmap, coronal_pixmap, axial_pixmap
    
    
    @staticmethod
    def add_wrap_to_str(string):
        max_len = 22
        if len(string) <= max_len:
            return string
        new_str = ""
        for i in range (0, len(string), max_len):
            new_str += string[i:i + max_len] + '\n'
        new_str = new_str[:-1]
        return new_str
    
    
    @staticmethod
    def save_file(vector, fileName):
        print(f"vector dimension: {vector.shape}")
        print(f"save path: {fileName}")
        np.savetxt(fileName, vector, fmt='%f')
    
        
    @staticmethod   
    def overlap(image:np.ndarray, attention_map:np.ndarray, alpha=0.7):
        # 缩放热力图适应原图
        zoom_factors = np.array((image.shape[0], image.shape[1], image.shape[2])) / np.array(attention_map.shape)
        attention_map = zoom(attention_map, zoom_factors, order=3, mode="reflect")  # order=3 代表三次样条插值
        
        # 归一化
        image = Util.normalize_image_0_to_1(image)
        attention_map = Util.normalize_image_0_to_1(attention_map)
        
        # 处理热力图
        cmap = colormaps['jet']  # 你可以选择其他颜色映射
        attention_map_colored = cmap(attention_map)
        attention_map_colored[..., -1] = attention_map
        attention_map = attention_map_colored
        
        # 将灰度图转换为 RGB
        image_rgb = np.stack([image] * 3, axis=-1)
        # 提取 RGBA 热力图的颜色和 alpha 通道
        color_layer = attention_map[..., :3]
        alpha_layer = attention_map[..., 3:]
        # 使用热力图的 alpha 通道来混合原图和热力图的颜色
        overlap_image = (alpha * alpha_layer) * color_layer + (1 - (alpha_layer * alpha)) * image_rgb
        return overlap_image
    
    
    @staticmethod
    def cal_paramters(model):
        # 计算模型的总参数量
        total_params = sum(p.numel() for p in model.parameters())

        print(f'Total number of parameters: {total_params}')
        # 计算可训练参数的总量
        trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
        # 计算非可训练参数的总量
        non_trainable_params = total_params - trainable_params

        print(f'Total number of trainable parameters: {trainable_params}')
        print(f'Total number of non-trainable parameters: {non_trainable_params}')
