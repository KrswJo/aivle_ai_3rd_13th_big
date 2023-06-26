from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('allauth.urls')),
    path('mypage/', views.mypage, name='mypage'),
     path('mypage_payment/', views.myreceipt_temp, name='myreceipt_temp'),
    path('myreceipt/<int:pk>', views.myreceipt, name='myreceipt')
]
