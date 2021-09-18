from django.http.response import HttpResponse
from PIL import Image
from django.shortcuts import render
from predictor.model.neural_net import predict
from predictor.models import ImagePicker
import requests
from math import ceil

def home(request):
    return render(request, 'predictor/index.html')

def verify(request):
    if request.method == 'POST':
        url_input = request.POST.get('url_input')
        file_input = request.FILES.get('file_input')
        if (url_input == '') and (file_input == ''):
            return render(request, 'predictor/verify.html', {'error': 'Please choose the image in either of the two formats'})
        else:
            if url_input:
                im = Image.open(requests.get(url_input, stream=True).raw)
                image = ImagePicker(image=im)
                image.save()
                result = predict(im)
                return results(request, result, image.get_url())
            elif file_input:
                image = ImagePicker(image = file_input)
                image.save()
                im = Image.open(image.image)
                result = predict(image_path=im)
                return results(request, result, image.get_url())
    return render(request, 'predictor/verify.html')


def results(request, result, image):
    filepath = image
    cgi_confidence = int(ceil(100.0 - result))
    pgi_confidence = int(ceil(result))
    status = ''
    if result > 50.0:
        status = 'TAMPERED'
    else:
        status = 'REAL'
    return render(request, 'predictor/results.html', {'tamper':cgi_confidence, 'photo':pgi_confidence, 'filepath':filepath, 'status': status})