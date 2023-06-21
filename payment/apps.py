from django.apps import AppConfig
from django.shortcuts import render
import subprocess

def object_detection(request):
    cmd = "python ../yolov5/detect.py --weights ../yolov5/pretrained_weights/yolov5m_costco10.pt --img 640 --conf 0.25 --source ../yolov5/data/images/test3.jpg"
    subprocess.run(cmd, shell=True)

    image_path = "../runs/detect/exp3/test3.jpg"
    image = Image.open(image_path)

    context = {'image': image}
    return render(request, '<html주소>.html', context)

class PaymentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "payment"
