from model import Simple3DCNN, Simple3DCNN_SimCLR, VoxVGG, VoxVGG_SimCLR, VoxResNet, VoxResNet_SimCLR
import torch

def net_simple_test():
    net = Simple3DCNN(class_nums=3)
    net.eval()
    test_input = torch.randn(2, 1, 100, 100, 100)
    test_output = net(test_input)
    print(test_output.shape)
    assert test_output.shape == torch.Size([2, 3])
    
    
def net_simplesimclr_test():
    net = Simple3DCNN_SimCLR(out_dim=1024)
    net.eval()
    test_input = torch.randn(2, 1, 100, 100, 100)
    test_output = net(test_input)
    print(test_output.shape)
    assert test_output.shape == torch.Size([2, 1024])
    

def net_voxvgg_test():
    net = VoxVGG(class_nums=5)
    net.eval()
    test_input = torch.randn(2, 1, 100, 100, 100)
    test_output = net(test_input)
    print(test_output.shape)
    assert test_output.shape == torch.Size([2, 5])
    

def net_voxvggsimclr_test():
    net = VoxVGG_SimCLR(out_dim=1024)
    net.eval()
    test_input = torch.randn(2, 1, 100, 100, 100)
    test_output = net(test_input)
    print(test_output.shape)
    assert test_output.shape == torch.Size([2, 1024])


def net_voxresnet_test():
    net = VoxResNet(class_nums=5)
    net.eval()
    test_input = torch.randn(2, 1, 100, 100, 100)
    test_output = net(test_input)
    print(test_output.shape)
    assert test_output.shape == torch.Size([2, 5])
    

def net_voxresnetsimclr_test():
    net = VoxResNet_SimCLR(out_dim=1024)
    net.eval()
    test_input = torch.randn(2, 1, 100, 100, 100)
    test_output = net(test_input)
    print(test_output.shape)
    assert test_output.shape == torch.Size([2, 1024])

net_simple_test()
net_simplesimclr_test()
net_voxvgg_test()
net_voxvggsimclr_test()
net_voxresnet_test()
net_voxresnetsimclr_test()
from util import Util
Util.cal_paramters(VoxVGG(class_nums=3))
Util.cal_paramters(VoxResNet(class_nums=3))
Util.cal_paramters(Simple3DCNN(class_nums=3))
Util.cal_paramters(Simple3DCNN_SimCLR(128))