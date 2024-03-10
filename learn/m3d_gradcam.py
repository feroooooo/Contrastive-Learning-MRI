# Setup the model
import torch
from torchvision import models, transforms
from torchvision.models import ResNet50_Weights
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# model = models.resnet152(weights=ResNet152_Weights.DEFAULT)
model = models.resnet50(weights=ResNet50_Weights.DEFAULT)

from medcam import medcam

model = medcam.inject(model, output_dir='attention_maps', backend='gcam', save_maps=False, return_attention=True)

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
print('predicted:', predicted)
print('attention_map shape:', attention_map.shape)

# 使用matplotlib可视化图像
# plt.imshow(attention_map, cmap='gray')
# plt.colorbar()  # 可选，为图像添加颜色条
# plt.show()
# plt.savefig('./attention_maps/fig.jpg')
plt.imsave('./attention_maps/heatmaps.jpg', attention_map)
resize_image = transforms.Resize((224, 224))(original_image)
resize_image.save('attention_maps/image.jpg')
image = np.array(resize_image)
print('image shape:' ,image.shape)


# 正规化热力图
attention_map_normalized = (attention_map - attention_map.min()) / (attention_map.max() - attention_map.min())

# 获取热力图颜色映射
cmap = colormaps['jet']  # 你可以选择其他颜色映射
attention_map_colored = cmap(attention_map_normalized)

# 将颜色映射的alpha值设置为热力图的正规化值，以创建透明度效果
# 这允许原始图像通过热力图显示
attention_map_colored[..., -1] = attention_map_normalized

# 创建一个图像来显示结果
fig, ax = plt.subplots()
ax.imshow(image)
ax.imshow(attention_map_colored, cmap='jet', alpha=0.8)  # 调整alpha以改变叠加层的透明度
plt.axis('off')  # 关闭坐标轴

# 保存叠加后的图像
plt.savefig('./attention_maps/superimposed_image.jpg', bbox_inches='tight', pad_inches=0)
plt.close(fig)  # 关闭图形，避免在Jupyter笔记本中显示
