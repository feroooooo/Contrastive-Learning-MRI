# 环境配置

```Shell
conda create -n mri python=3.11
conda install -c conda-forge nibabel
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
conda install pandas
conda install matplotlib
pip install tensorboard -U
```

# TensorBoard

- 启动
  - tensorboard --logdir=logs
- url
  - http://localhost:6006
我有一个ADNI的结构MRI数据集，我现在想将其分为训练集、验证集、测试集三部分，比例分别为70%，15%，15%，对于验证集和测试集，其最小占比的类别不得少于30%。该数据集的标签由csv文件提供，共有image_id，subject，group三个字段，image_id代表图像的id，同时也是图像文件名，subject代表被试id，group代表该图像的类别，共有AD，MCI，CN三种。目前已知数据集总数为3960，被试个数为980，相同被试不同时间获得的图像的group相同。注意：每个subject对应的数据数量并不相同，同时需要确保相同的subject对应的图像需在同一个集合中。