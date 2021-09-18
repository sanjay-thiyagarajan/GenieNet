from django.http.response import HttpResponse
from django.shortcuts import render
from predictor.model.neural_net import predict
def home(request):
    op = predict('')
    return HttpResponse(op)
