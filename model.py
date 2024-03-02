import torch
import torch.nn as nn
import torch.nn.functional as F

# 定义CNN网络结构
class Simple3DCNN(nn.Module):
    def __init__(self):
        super(Simple3DCNN, self).__init__()
        self.conv1 = nn.Conv3d(1, 8, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool3d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv3d(8, 16, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(16 * 22 * 27 * 22, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 3)  # Assuming 3 classes for CN, MCI, and AD

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 22 * 27 * 22)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
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


if __name__ == '__main__':
    net = VGG3D()
    net.eval()
    # Generate a random test input tensor of the size (1, 91, 109, 91)
    test_input = torch.randn(1, 1, 91, 109, 91)

    # Forward pass through the network
    test_output = net(test_input)
    print(test_output)