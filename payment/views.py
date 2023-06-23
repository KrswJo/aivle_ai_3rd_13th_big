from django.shortcuts import render
from django.utils import timezone
import logging
from django.conf import settings
from django.core.files.storage import default_storage
import numpy as np
import cv2
import string
import mlflow
import mlflow.keras
# from chatgpt.views import chatGPT
logger = logging.getLogger('mylogger')
#signlanguage/models.py의 Result 모델을 import한다.
from .models import PaymentResult, Result, CostcoPrice, receipt
from .apps import object_detection
# Create your views here.

'''
1. 원칙은 ORM을 사용하여 별도 sql 문이 없는 것이다.
2. 하지만, ORM을 사용하면서도 sql문을 사용해야 하는 경우가 있다.
3. 이때는 아래와 같이 사용한다.
 - 물론 이 부분도 view가 sql을 알면 안되서 분리해야 하지만, 짧은 교육상 이곳에 둔다. 
'''


def index(request):
    return render(request, 'payment/index.html')




def result(request):
    if request.method == 'POST' and request.FILES['files']:

        results=[]
        #form에서 전송한 파일을 획득한다.
        #각 파일별 예측 결과들을 모아야 질문을 위한 언어가 완성된다.
        files = request.FILES.getlist('files')
        chatGptPrompt = ""
        for idx,file in enumerate(files, start=0):
            #######MLflow에서 모델 로딩 후 이미 전처리하여 예측한 결과 텍스트를 변수에 저장##########
            # # logger.error('file', file)
            # # class names 준비
            # class_names = list(string.ascii_lowercase)
            # class_names = np.array(class_names)

            
            # # mlflow 로딩
            # mlflow_uri="http://mini7-mlflow.carpediem.so/"
            # mlflow.set_tracking_uri(mlflow_uri)
            # model_uri = "models:/Sign_Signal/production"
            # model = mlflow.keras.load_model(model_uri)


            # # history 저장을 위해 객체에 담아서 DB에 저장한다.
            # # 이때 파일시스템에 저장도 된다.
            # result = Result()
            # result.image = file
            # result.pub_date = timezone.datetime.now()
            # result.save()


            # # 흑백으로 읽기
            # img = cv2.imread(result.image.path, cv2.IMREAD_GRAYSCALE)

            # # 크기 조정
            # img = cv2.resize(img, (28, 28))

            # # input shape 맞추기
            # test_sign = img.reshape(1, 28, 28, 1)

            # # 스케일링
            # test_sign = test_sign / 255.

            # # 예측 : 결국 이 결과를 얻기 위해 모든 것을 했다.
            # pred = model.predict(test_sign)
            # pred_1 = pred.argmax(axis=1)

            # result_str = class_names[pred_1][0]


            object_detection(request,file)

            
            
            
            purchased_products = dict()
            purchased_products_weights = 0
            purchased_products_price = 0
            with open('./detect_products/exp/labels/Products.txt', 'r') as file:
                lines = file.readlines()  # 파일의 모든 줄을 읽어옴
                if lines[0] != 'NO_DETECT':
                    #Order.objects.create(member = request.user)
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
                            
                    for purchased_product in purchased_products:
                        print(purchased_product,'\t\t\t개수:',purchased_products[purchased_product][0],'\t\t\t가격:',purchased_products[purchased_product][1])
                        #receipt().objects.create(names = purchased_product, count_quantity=purchased_products[purchased_product][0], price=purchased_products[purchased_product][1])
                        receipt.objects.create(names = purchased_product, count_quantity=purchased_products[purchased_product][0], member = request.user, price=purchased_products[purchased_product][1])
                    print('총가격:',purchased_products_price)
                    print('총무게:',purchased_products_weights)
                else:
                    print('왜 아무것도 안사요 ㅡ,ㅡ')
                    

                    
            # #결과를 DB에 저장한다.
            # result.result = result_str
            # # result.is_correct = 
            # result.save()
            # results.append(result)

            # #result.result의 결과를 하나씩 chatGptPrompt에 추가한다.
            # chatGptPrompt += result.result
        
    #     #질문을 DB에 저장한다.
    #     chatResult = ChatResult()
    #     chatResult.prompt = chatGptPrompt
    #     chatResult.pub_date = timezone.datetime.now()
    #     chatResult.save()


    #     #저장된 질문을 DB에서 가져온다.
    #     selectedChatResult = ChatResult.objects.get(id=chatResult.id)

    #     #chatGptPrompt를 chatGPT에게 전달한다.
    #     content = chatGPT(selectedChatResult.prompt)
    #     selectedChatResult.content = content
    #     selectedChatResult.save()
        
     

    #     context = {
    #     'question': selectedChatResult.prompt,
    #     'result': selectedChatResult.content
    # }
    
    receipts = receipt.objects.all()
    
    context = {
        'purchased_products_weights' : purchased_products_weights,
        'purchased_products_price' : purchased_products_price,
        'receipts':receipts
    }
    
    weights_test = 100
    if weights_test != purchased_products_weights:
        return render(request, 'payment/result.html', context)  
    else:
        return render(request, 'payment/result.html', context)  


def test(request):

        
        
    return render(request, 'payment/result.html')