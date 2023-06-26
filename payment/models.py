from django.db import models
import uuid

# Create your models here.

    
class CostcoPrice(models.Model):
    idx = models.AutoField(primary_key=True)
    names = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    weight = models.CharField(max_length = 50)
    
    class Meta:
        managed = False
        db_table = 'costco_price'
    
class receipt(models.Model):
    names = models.TextField(null=True)
    price = models.TextField(null=True)
    count_quantity = models.TextField(null=True)
    member = models.ForeignKey("member.User", on_delete = models.CASCADE)
    
class Order(models.Model):
    date = models.DateTimeField(auto_now_add = True)
    Order_id = models.UUIDField(default=uuid.uuid4, editable=False)
    member = models.ForeignKey("member.User", on_delete = models.CASCADE)
    receipts = models.ForeignKey(receipt, on_delete=models.CASCADE)