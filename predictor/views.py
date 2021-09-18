from django.http.response import HttpResponse
from PIL import Image
from django.shortcuts import render
from predictor.model.neural_net import predict
from predictor.models import ImagePicker
import requests
from math import floor

def home(request):
    return render(request, 'predictor/index.html')

def verify(request):
    if request.method == 'POST':
        url_input = request.POST.get('url_input')
        file_input = request.FILES.get('file_input')
        if (url_input == '') and (file_input == ''):
            return render(request, 'predictor/verify.html', {'error': 'Please choose the image in either of the two formats'})
        else:
            image_path = 'GenieNet/static/img/input_image.jpg'
            if url_input:
                im = Image.open(requests.get(url_input, stream=True).raw)
                im = im.convert('RGB')
                im.save(image_path)
                result = predict(im)
                return results(request, result, '/img/input_image.jpg')
            elif file_input:
                im = Image.open(file_input)
                im = im.convert('RGB')
                im.save(image_path)
                result = predict(im)
                return results(request, result, '/img/input_image.jpg')
    return render(request, 'predictor/verify.html')


def results(request, result, image):
    filepath = image
    cgi_confidence = int(floor(100.0 - result))
    pgi_confidence = int(floor(result))
    status = ''
    if result < 50.0:
        status = 'TAMPERED'
    else:
        status = 'REAL'
    return render(request, 'predictor/results.html', {'tamper':cgi_confidence, 'photo':pgi_confidence, 'filepath':filepath, 'status': status})