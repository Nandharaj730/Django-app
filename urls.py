from re import template
from django.contrib import admin  
from django.urls import path
from . import views
import nandhaapp

urlpatterns = [
    path('admin/', admin.site.urls) ,
    path('Forms/' , views.Forms) ,
    path('' , views.sayHello) ,
    path('database/' , views.getFile) ,
    path('index.html' , views.index) ,
    ]