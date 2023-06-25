from django.shortcuts import render, get_object_or_404
from django.db import connection
from .models import User
from payment.models import Order, receipt
import json

# Create your views here.
def mypage(request):
        # member_user 테이블의 레코드를 가져와서 객체로 다룹니다.
    current_user = User.objects.get(pk = request.user.pk) #username: janggh1012
    Orders = Order.objects.filter(member=request.user)
    
    context = {
        'current_user': current_user,
        'Orders':Orders       
    }

    return render(request, 'account/mypage.html',context)

def myreceipt(request, pk):
    receipt_list = get_object_or_404(receipt, pk=pk)
    
    
    jsonDec = json.decoder.JSONDecoder()
    name_list = jsonDec.decode(receipt_list.names)
    count_quantity_list = jsonDec.decode(receipt_list.count_quantity)
    price_list = jsonDec.decode(receipt_list.price)
    total_price = sum(price_list)
    receipts_list = zip(name_list, price_list, count_quantity_list)
    
    context = {
        'receipts_list': receipts_list,
        'total_price':total_price
    }
    
    return render(request, 'account/myreceipt.html', context)