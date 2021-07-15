from Task_API.urls import *
from django.contrib import admin
from django.urls import path
from .views import *
from Task_API.urls import *

urlpatterns = [
    path('',TaskAPIView.as_view(),name="Tasks"),
    path('<int:pk>', TaskDetailsAPIView.as_view(), name='Task_Details'),
    path('tags',TagAPIView.as_view()),
    path('tags/<int:pk>',TagDetailsAPIView.as_view())
]
