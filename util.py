import numpy as np
import math

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

        saggital_img = np.rot90(nii_img[x, :, :][:, ::-1], k=3)
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
    def add_wrap_to_str(string):
        max_len = 25
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