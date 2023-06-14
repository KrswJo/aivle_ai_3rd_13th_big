from django.urls import path

from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('create/', views.create, name="create"),
    path('detail/<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('detail/<int:pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]