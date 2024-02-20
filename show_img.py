import nibabel as nib
import matplotlib.pyplot as plt

file_path = 'C:/Users/Fero/Desktop/brain_adni_0021_I196077_fsld.nii.gz'

# 使用nibabel加载nii.gz文件
nii_image = nib.load(file_path)

# 获取图像数据为numpy数组
image_data = nii_image.get_fdata()

# 打印图像维度
print("Image shape:", image_data.shape)

# 可视化每一层切片
num_slices = image_data.shape[-1]

# 设置子图的行数和列数
num_rows = num_slices // 10 + 1  # 每行显示10个切片
num_cols = min(num_slices, 10)

# 设置子图的大小
fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 15))

# 遍历每一层切片并可视化
for i in range(num_slices):
    row_idx = i // 10
    col_idx = i % 10

    # 在子图中显示每一层切片
    axes[row_idx, col_idx].imshow(image_data[:, :, i], cmap='gray')
    axes[row_idx, col_idx].axis('off')  # 关闭坐标轴

# 如果切片数量不是10的倍数，隐藏多余的子图
for i in range(num_slices, num_rows * num_cols):
    row_idx = i // 10
    col_idx = i % 10
    fig.delaxes(axes[row_idx, col_idx])

plt.show()

# 保存切片
print(f"num of slices:{num_slices}")
plt.clf()
for i in range(num_slices):
    # plt.imshow(image_data[:, :, i])
    plt.imsave(f"./image/slice_{i+1}.jpg", image_data[:, :, i], cmap='gray')
    



# 查看图像大小
height, width, depth = image_data.shape
print(f"The image object height: {height}, width:{width}, depth:{depth}")
# 查看图像值范围
print(f'image value range: [{image_data.min()}, {image_data.max()}]')

# 查看图像成像信息，如 层厚，平面（in-plane）分辨率等

# 矩阵以外的信息可以通过 image_obj.header 获取

# header是键值对，查看 header 包含的所有信息
print('headers', nii_image.header.keys())
# 查看成像信息
pixdim = nii_image.header['pixdim']
print(f'z轴分辨率： {pixdim[3]}')
print(f'in plane 分辨率： {pixdim[1]} * {pixdim[2]}')
x_range = pixdim[1] * height
y_range = pixdim[2] * width
z_range = pixdim[3] * depth
print(f"The image object x_range: {x_range}, y_range:{y_range}, z_range:{z_range}")
# 整个数据
print('img1_obj', nii_image)