from django.urls import path
from . import views


urlpatterns = [
    #Главная страница - posts
    path('', views.index),
    path('group/<slug:slug>/', views.group_posts)
]