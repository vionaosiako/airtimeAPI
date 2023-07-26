from django.urls import path
from .views import *

urlpatterns =[
    path('',sendAirtime,name='airtime'),
]