# Setup the model
import torch
from torchvision import models, transforms
from torchvision.models import ResNet50_Weights
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# model = models.resnet152(weights=ResNet152_Weights.DEFAULT)
model = models.resnet50(weights=ResNet50_Weights.DEFAULT)

from medcam import medcam

model = medcam.inject(model, output_dir='attention_maps', backend='gcam', layer='layer4', label='best', save_maps=False, return_attention=True)

transform = transforms.Compose([
    transforms.Resize((224, 224)),  # 示例尺寸，根据需要调整
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # ImageNet标准化
])

img_path = r"C:\Users\MSi\Pictures\both.png"
original_image = Image.open(img_path).convert('RGB')
# 预处理图片
image = transform(original_image)
# 增加一个批次维度，因为PyTorch模型通常期望批次输入
image = image.unsqueeze(0)
        
model.eval()
with torch.no_grad():
    # 进行预测
    outputs, attention_map = model(image)
    # 输出处理，获取预测结果
    _, predicted = torch.max(outputs, 1)
    attention_map = attention_map.detach().cpu().numpy()
attention_map = np.squeeze(attention_map)
print(attention_map.shape)
print(predicted)

# 使用matplotlib可视化图像
plt.imshow(attention_map, cmap='gray')
plt.colorbar()  # 可选，为图像添加颜色条
# plt.show()
plt.savefig('./attention_maps/fig.jpg')
plt.imsave('./attention_maps/heatmaps.jpg', attention_map, cmap='gray')