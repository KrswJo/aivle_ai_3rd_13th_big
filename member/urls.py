from django.urls import path, include
from . import views

app_name = 'member'
urlpatterns = [
    path('', include('allauth.urls')),
    path('mypage/', views.mypage, name='mypage'),
    path('myreceipt/<int:pk>', views.myreceipt, name='myreceipt')
]
