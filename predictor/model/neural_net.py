from PIL import Image
from torchvision import transforms
import torch.nn as nn
import torch

class ConvNet(nn.Module): 
        def __init__(self, input_dim):
            super(ConvNet, self).__init__()
            self.layer1 = nn.Sequential(
                nn.Conv2d(3, 32, kernel_size=5, stride=1, padding=4),
                nn.BatchNorm2d(32),
                nn.ReLU(),
                nn.MaxPool2d(kernel_size=5, stride=2))
            self.layer2 = nn.Sequential(
                nn.Conv2d(32, 64, kernel_size=5, stride=1, padding=4),
                nn.BatchNorm2d(64),
                nn.ReLU(),
                nn.MaxPool2d(kernel_size=5, stride=2))
            self.layer3 = nn.Sequential(
                nn.Conv2d(64, 128, kernel_size=5, stride=2, padding=6),
                nn.BatchNorm2d(128),
                nn.ReLU(),
                nn.MaxPool2d(kernel_size=5, stride=2))
            self.layer4 = nn.Sequential(
                nn.Conv2d(128, 256, kernel_size=5, stride=2, padding=6),
                nn.BatchNorm2d(256),
                nn.ReLU(),
                nn.MaxPool2d(kernel_size=5, stride=2))
            self.fc1 = nn.Sequential(
                nn.Linear(int(input_dim/8) * int(input_dim/8) * 4, 64),
                nn.ReLU())
            self.fc2 = nn.Sequential(
                nn.Linear(64, 1),
                nn.Sigmoid())

        def forward(self, x):
            out = self.layer1(x)
            out = self.layer2(out)
            out = self.layer3(out)
            out = self.layer4(out)
            out = out.reshape(out.size(0), -1)
            out = self.fc1(out)
            out = self.fc2(out)
            return out


def predict(image_path):

    INPUT_DIM = 256

    preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )])

    pretrained_model = ConvNet(INPUT_DIM)
    pretrained_model.load_state_dict(torch.load('predictor/model/pretrained_model.pth', map_location=torch.device('cpu')))

    im = Image.open(image_path)

    im_preprocessed = preprocess(im)

    batch_img_tensor = torch.unsqueeze(im_preprocessed, 0)

    output = pretrained_model(batch_img_tensor)

    confidence = float(output.data[0])
    
    return confidence