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
    
class CostcoPrice(models.Model):
    idx = models.AutoField(primary_key=True)
    names = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'costco_price'