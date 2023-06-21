from django.db import models

# Create your models here.



class Result(models.Model):
    image = models.ImageField(blank=True)
    answer = models.CharField(max_length=10,null=True)
    result = models.CharField(max_length=10)
    is_correct= models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
class PaymentResult(models.Model):
    prompt = models.CharField(max_length=1000)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    
# class CameraImage(models.Model):
#     image = models.ImageField(upload_to="static/img/")
#     timestamp = models.DateTimeField(auto_now_add=True)