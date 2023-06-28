from django.shortcuts import render, redirect
from django.utils import timezone
import logging
from django.conf import settings
from django.core.files.storage import default_storage
import numpy as np
import cv2
import string
logger = logging.getLogger('mylogger')
from .models import CostcoPrice, receipt, Order
from .apps import object_detection

import simplejson as json

def index(request):
    return render(request, 'payment/index.html')

def result(request):
    if request.method == 'POST' and request.FILES['files'] and request.user.is_authenticated:

        results=[]
        files = request.FILES.getlist('files')
        chatGptPrompt = ""
        for idx,file in enumerate(files, start=0):

            object_detection(request,file)

            purchased_products = dict()
            purchased_products_weights = 0
            purchased_products_price = 0
            with open('./detect_products/exp/labels/Products.txt', 'r') as file:
                lines = file.readlines()  # 파일의 모든 줄을 읽어옴
                if lines[0] != 'NO_DETECT':
                    for line in lines:
                        product_id = int(line.strip().split()[0]) + 1
                        product = CostcoPrice.objects.get(idx=product_id)
                        product_name = product.names
                        product_price = product.price
                        purchased_products_weights += product.weight
                        purchased_products_price += product_price
                        if product_name in purchased_products:
                            purchased_products[product_name][0] += 1
                            purchased_products[product_name][1] += product_price
                        else:
                            purchased_products[product_name] = [1,product_price]
                            
                    name_list = []
                    price_list = []
                    count_quantity_list = []

                    for purchased_product, values in purchased_products.items():
                        print(purchased_product,'\t\t\t개수:',values[0],'\t\t\t가격:',values[1])
                        name_list.append(purchased_product)
                        price_list.append(values[1])
                        count_quantity_list.append(values[0])
                        
                    receipts = receipt()
                    receipts.names = json.dumps(name_list)
                    receipts.price = json.dumps(price_list)
                    receipts.count_quantity = json.dumps(count_quantity_list)
                    receipts.member = request.user
                    receipts.save()
                    
                    print('총가격:',purchased_products_price)
                    print('총무게:',purchased_products_weights)
                else:
                    print('왜 아무것도 안사요 ㅡ,ㅡ')
                    return render(request, 'payment/fail.html')
    
        receipts = receipt.objects.all()
        receipts_list = zip(name_list, price_list, count_quantity_list)
        
        context = {
            'purchased_products_weights' : purchased_products_weights,
            'purchased_products_price' : purchased_products_price,
            'receipts_list':receipts_list
        }
        with open('./detect_products/exp/labels/Weights.txt', 'r') as file:
            weights_test = file.readline()
            weights_test = int(weights_test)

        weights_test = purchased_products_weights
        if weights_test != purchased_products_weights:
            # 지우지 말 것
            # last_receipt = receipt.objects.latest('id')
            # last_receipt.delete()
            # return render(request, 'payment/fail.html', context)
            
            # 임시
            return render(request, 'payment/fail.html', context)
        else:
            return render(request, 'payment/result.html', context)
    else:
        return render(request, 'payment/fail.html')

def complete(request):
    receipt_result = receipt.objects.filter(member=request.user).latest('id')
    order = Order(receipts=receipt_result, member=request.user)
    order.save()

    return render(request, 'payment/complete.html')

def fail(request):
    return render(request, 'payment/fail.html')
