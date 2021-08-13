from Task_API.urls import *
from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>',partial_update,name='partial')
]
