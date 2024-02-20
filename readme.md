# 环境配置
```Shell
conda create -n mri python=3.11
conda install -c conda-forge nibabel
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
conda install pandas
conda install matplotlib
conda install tensorboard
```

# TensorBoard
- 启动
  - tensorboard --logdir=logs
- url
  - http://localhost:6006