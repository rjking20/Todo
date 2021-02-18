
from django.contrib import admin
from django.urls import path
from .views import home,update,delete

urlpatterns = [

    path('',home,name='home'),
    path('update/<pk>/',update,name='update'),
    path('delete/<pk>/',delete,name='delete'),
]
