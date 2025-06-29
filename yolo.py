import pandas as pd
%cd /content/drive/MyDrive/YOLO
!unzip "/content/drive/MyDrive/YOLO/archive.zip" -d "/content/drive/MyDrive/YOLO/unzip"
%pip install ultralytics
from ultralytics import YOLO
model=YOLO("yolov5s.pt")
model.train(data="/content/drive/MyDrive/YOLO/data.yaml",epochs=10,imgsz=640)
model=YOLO("/content/runs/detect/train/weights/best.pt")
result=model("/content/drive/MyDrive/YOLO/unzip/vehicle dataset/train/images/05817_Nissan NV Passenger Van 2012.jpg")
result[0].show()