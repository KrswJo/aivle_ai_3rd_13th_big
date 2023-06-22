from django.apps import AppConfig
from django.shortcuts import render, redirect
from PIL import Image
import subprocess
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

def object_detection(request,file):
    
    image = Image.open(file)
    image.save("./media/Products.jpg","JPEG")

    STR_BASE_DIR = str(BASE_DIR)
    cmd = "python " + STR_BASE_DIR + "/yolov5/detect.py --weights " + STR_BASE_DIR + "/yolov5/pretrained_weights/yolov5m_costco10.pt --img 640 --conf 0.25 --img 640 --conf 0.25 --source " + STR_BASE_DIR + "/media/Products.jpg"
    subprocess.run(cmd, shell=True)

    # context = {'image': image}
    # return render(request, 'payment/result.html', context)
    return render(request, '/payment/result.html')


class PaymentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "payment"

