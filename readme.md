毕设

# 环境配置

```Shell
conda create -n mri python=3.11
conda install -c conda-forge nibabel
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
conda install pandas
conda install matplotlib
pip install tensorboard -U
conda install -c conda-forge monai
conda install scikit-learn
conda install tqdm
pip install medcam
```

# TensorBoard

- 启动
  - tensorboard --logdir=logs
- url
  - http://localhost:6006

# 记录

- 未根据被试进行集合划分时
  - accuracy：90%（存在信息泄露）
- 根据被试划分后
  - accuracy：50%（过拟合）
- 数据增强后
  - accuracy：50%（过拟合）

# 问题

- 进行调整对比度等操作时，使原先的全黑（为 0）像素发生了变化，从而导致正则化时 nonzero 参数无法正确识别纯黑背景（尝试取消 nonzero）
- 图像存在大量全黑切片
