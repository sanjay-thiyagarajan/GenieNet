from django.urls import path
from predictor.views import *

urlpatterns = [
    path('', home, name='home'),
    path('verify/', verify, name='verify'),
    path('results/', results, name='results')

]
