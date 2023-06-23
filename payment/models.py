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
    weight = models.CharField(max_length = 50)
    
    class Meta:
        managed = False
        db_table = 'costco_price'
    
class receipt(models.Model):
    idx = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add = True)
    names = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    member = models.ForeignKey("member.User", on_delete = models.CASCADE)
    count_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payment_receipt'
        