import torch
from model import VoxVGG

args = {}
args['arch'] = 'vgg'
args['weight_path'] = 'runs'
args['data_path'] = ''
args['csv_train_path'] = ''
args['csv_validation_path'] = ''
args['csv_test_path'] = ''

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = VoxVGG(class_nums=3).to(device)