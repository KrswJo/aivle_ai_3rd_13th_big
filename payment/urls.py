# payment/urls.py
from django.urls import path
from . import views

app_name = 'payment'
urlpatterns = [
    path('', views.index, name='index'),
    #path('result', views.result, name='result'),
    path('test/', views.test, name='test'),
    path('test/upload', views.upload, name='upload'),
    path('result', views.result, name='result'),
    path('prototype', views.prototype, name='result'),
    path('capture/', views.capture_image, name='capture_image'),
]
