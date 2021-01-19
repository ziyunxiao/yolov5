import torch
from PIL import Image

# Model
model = torch.hub.load(
    "ultralytics/yolov5",
    "yolov5s",
    pretrained=True,
)

# Images
img1 = Image.open("data/images/zidane.jpg")
img2 = Image.open("data/images/bus.jpg")
imgs = [img1, img2]  # batched list of images

# Inference
result = model(imgs)

print(result)
