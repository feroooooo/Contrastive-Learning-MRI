# Environment

```Shell
conda create -n mri python=3.11
conda activate mri

conda install -c conda-forge nibabel
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
conda install pandas
conda install matplotlib
pip install tensorboard -U
conda install -c conda-forge monai
conda install scikit-learn
conda install tqdm
pip install medcam
pip install pyside6
```

# TensorBoard

- Start
  - tensorboard --logdir=$logdir$
- url
  - http://localhost:6006

# Visualize

- Start
  - python main_ui.py

# File Description

- learn
  - description
    - 学习与测试脚本，可删除
- ui
  - description
    - ui 相关文件
  - files
    - resource
      - 资源文件
    - icon.ico
      - 应用 ico
    - main.ui
      - QtDesigner 界面文件
    - Ui_main.py
      - 通过 uic 将 main.ui 编译为 py 文件得到
    - resource.qrc
      - QtDesigner 资源配置文件
    - resource_rc.py
      - 通过 rcc 将 resource.qrc 编译为 py 文件得到
- checkpoint
  - 包含权重文件，运行 eval_simclr.py 得到
- runs
  - description
    - 每次训练的记录（包含分类模型和对比学习模型）
  - files
    - checkpoint.pth
      - 权重文件
    - config.yaml
      - 超参记录
    - training.log
      - 训练日志
    - events.out.tfevents.$paramters$
      - tensorboard 记录
  - data_augmentation.py
    - 数据预处理和增强方法
  - eval_classification.py
    - 对分类模型进行评价
  - eval_simclr.py
    - 对 simclr 模型进行评价（线性分类得到的特征）
  - eval.ipynb
    - 同上，训练方式较简单
  - main_ui.py
    - 可视化应用入口
  - model.py
    - 模型
  - mri_dataset.py
    - 数据集
  - predict.py
    - 对模型预测进行包装
  - process_dataset.py
    - 数据集分割
  - readme.md
    - 相关说明，此文件
  - system_config.json
    - 可视化应用设置
  - test.ipynb
    - 临时测试脚本，可删除
  - test.py
    - 测试模块
  - todo.md
    - 待办列表
  - tran_classification.py
    - 分类模型训练
  - train_simclr.ipynb
    - simclr 训练
  - util.py
    - 工具类
  - visualize.ipynb
    - 可视化脚本

# 打包

- pip install pyinstaller
- pyinstaller -D -i ./ui/icon.ico main_ui.py -n 基于对比学习的脑结构磁共振影像特征提取系统 --noconsole --clean --exclude-module PyQt5
