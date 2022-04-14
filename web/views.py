from django.shortcuts import render
# import onnx, onnxruntime, pathlib, json
# from keras.preprocessing import image
# import numpy as np
from .forms import Form


def index(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = Form()
    return render(request, 'index.html', {'form': form})
