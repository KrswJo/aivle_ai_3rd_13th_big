# payment/urls.py
from django.urls import path
from . import views

app_name = 'payment'
urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('complete/', views.complete, name='complete'),
    path('fail/', views.fail, name='fail'),
]
