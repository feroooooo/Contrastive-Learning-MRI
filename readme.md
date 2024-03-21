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
