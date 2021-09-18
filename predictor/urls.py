from django.urls import path
from predictor.views import *

urlpatterns = [
    path('', home, name='home')
]
