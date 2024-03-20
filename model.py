import torch
import torch.nn as nn
import torch.nn.functional as F


class Simple3DCNN(nn.Module):
    def __init__(self, class_nums):
        super(Simple3DCNN, self).__init__()
        self.conv1 = nn.Conv3d(1, 8, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool3d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv3d(8, 16, kernel_size=3, stride=2, padding=1)
        self.last_fc = nn.Linear(16 * 12 * 12 * 12, class_nums)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 12 * 12 * 12)
        x = self.last_fc(x)
        return x



# out_dim为计算损失时的维度，训练完毕推理时输出的维度为dim_mlp
class Simple3DCNN_SIMCLR(nn.Module):
    def __init__(self, out_dim):
        super(Simple3DCNN_SIMCLR, self).__init__()
        self.backbone = Simple3DCNN(out_dim)
        dim_mlp = self.backbone.last_fc.in_features
        self.backbone.last_fc = nn.Sequential(nn.Linear(dim_mlp, dim_mlp), nn.ReLU(), self.backbone.last_fc)

    def forward(self, x):
        x = self.backbone(x)
        return x


# VoxVGG
class VGG3D(nn.Module):
    def __init__(self):
        super(VGG3D, self).__init__()
        
        # Define the layers
        self.conv1 = nn.Conv3d(in_channels=1, out_channels=8, kernel_size=3)
        self.conv2 = nn.Conv3d(8, 8, 3)

        self.conv3 = nn.Conv3d(8, 16, 3)
        self.conv4 = nn.Conv3d(16, 16, 3)

        self.conv5 = nn.Conv3d(16, 32, 3)
        self.conv6 = nn.Conv3d(32, 32, 3)
        self.conv7 = nn.Conv3d(32, 32, 3)

        self.conv8 = nn.Conv3d(32, 64, 3)
        self.conv9 = nn.Conv3d(64, 64, 3)
        self.conv10 = nn.Conv3d(64, 64, 3)

        self.fc1 = nn.Linear(64, 128)
        self.bn1 = nn.BatchNorm1d(128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 3) 

    def forward(self, x):
        # Define the forward pass
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.max_pool3d(x, 2)

        x = F.relu(self.conv3(x))
        x = F.relu(self.conv4(x))
        x = F.max_pool3d(x, 2)

        x = F.relu(self.conv5(x))
        x = F.relu(self.conv6(x))
        x = F.relu(self.conv7(x))
        x = F.max_pool3d(x, 2)

        x = F.relu(self.conv8(x))
        x = F.relu(self.conv9(x))
        x = F.relu(self.conv10(x))
        x = F.max_pool3d(x, 2)

        # Flatten the output for the dense layer
        x = torch.flatten(x, 1)
        
        x = F.dropout(F.relu(self.bn1(self.fc1(x))), 0.7)
        x = F.relu(self.fc2(x))
        x = self.fc3(x)

        return x


# VoxResNet
class VoxResNet(nn.Module):
    def __init__(self):
        super(VoxResNet, self).__init__()
        # Initial Convolution Block
        self.conv1a = nn.Conv3d(1, 32, kernel_size=3, padding=1)
        self.bn1a = nn.BatchNorm3d(32)
        self.conv1b = nn.Conv3d(32, 32, kernel_size=3, padding=1)
        self.bn1b = nn.BatchNorm3d(32)
        # self.conv1c = nn.Conv3d(32, 64, kernel_size=3, stride=2, padding=56)
        self.conv1c = nn.Conv3d(32, 64, kernel_size=3, stride=2, padding=2)
        # VoxRes Blocks
        self.voxres2 = self._voxres_block(64, 64)
        self.voxres3 = self._voxres_block(64, 64)
        self.conv4 = nn.Conv3d(64, 64, kernel_size=3, stride=2, padding=2)
        self.voxres5 = self._voxres_block(64, 64)
        self.voxres6 = self._voxres_block(64, 64)
        self.conv7 = nn.Conv3d(64, 128, kernel_size=3, stride=2, padding=2)
        self.voxres8 = self._voxres_block(128, 128)
        self.voxres9 = self._voxres_block(128, 128)
        # Final Layers
        # self.pool10 = nn.AdaptiveAvgPool3d((1, 1, 1))
        self.fc11 = nn.Linear(1024, 128)
        self.prob = nn.Linear(128, 3)

    def _voxres_block(self, in_channels, out_channels):
        layers = nn.Sequential(
            nn.BatchNorm3d(in_channels),
            nn.ReLU(inplace=True),
            nn.Conv3d(in_channels, out_channels, kernel_size=3, padding='same'),
            nn.BatchNorm3d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv3d(out_channels, out_channels, kernel_size=3, padding='same'),
        )
        return layers

    def forward(self, x):
        # 卷积padding待确定
        x = F.relu(self.bn1a(self.conv1a(x)))
        x = F.relu(self.bn1b(self.conv1b(x)))
        x1 = self.conv1c(x)
        

        x2 = self.voxres2(x1) + x1
        x3 = self.voxres3(x2) + x2
        

        x4 = F.relu(self.conv4(x3))

        x5 = self.voxres5(x4) + x4
        x6 = self.voxres6(x5) + x5

        x7 = F.relu(self.conv7(x6))
        x8 = self.voxres8(x7) + x7
        x9 = self.voxres9(x8) + x8
        # 最大池化
        x = F.max_pool3d(x9, 8)
        x = torch.flatten(x, 1)
        # x = self.pool10(x9).view(x9.size(0), -1)
        x = F.relu(self.fc11(x))
        x = self.prob(x)

        return x




if __name__ == '__main__':
    # net = VGG3D()
    net = Simple3DCNN()
    net.eval()
    # Generate a random test input tensor of the size (1, 91, 109, 91)
    test_input = torch.randn(2, 1, 100, 100, 100)

    # Forward pass through the network
    test_output = net(test_input)
    print(test_output.shape)