import numpy as np

class Predictor:
    def __init__(self) -> None:
        pass
    
    
    def extract(self, nii_img:np.ndarray) -> np.ndarray:
        """_summary_

        Args:
            nii_img (np.ndarray): (91 x 109 x 91)

        Returns:
            np.ndarray: (128)
        """
        print(f"image dimension: {nii_img.shape}")
        random_normal_array = np.random.randn(128)
        return random_normal_array