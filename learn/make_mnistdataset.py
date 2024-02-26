from torchvision import datasets

#下载测试集
train_dataset = datasets.MNIST('./data', train=True,
                                download=True)
test_dataset =  datasets.MNIST('./data', train=False, 
                                download=True)

with open('./MNIST/train_label.csv', 'w') as file:
    file.write("file_name,label\n")
with open('./MNIST/train_label.csv', 'a') as file:
    for i in range(len(train_dataset)):
        train_dataset[i][0].save(f"./MNIST/train/{i+1}.jpg")
        file.write(f"{i+1}.jpg,{train_dataset[i][1]}\n")

with open('./MNIST/test_label.csv', 'w') as file:
    file.write("file_name,label\n")
with open('./MNIST/test_label.csv', 'a') as file:
    for i in range(len(test_dataset)):
        test_dataset[i][0].save(f"./MNIST/test/{i+1}.jpg")
        file.write(f"{i+1}.jpg,{test_dataset[i][1]}\n")