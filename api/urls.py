from Task_API.urls import *
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('test/<int:pk>',test,name='test'),
]
