from ultralytics import YOLO
model=YOLO(r"C:\Users\Rihan\Desktop\richu\copy\best.pt")
result=model(r"C:\Users\Rihan\Desktop\richu\download.jpeg")
result[0].show()