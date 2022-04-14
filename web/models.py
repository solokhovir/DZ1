from django.db import models


class Recognize(models.Model):
    # onnx = models.FileField(upload_to='onnx')
    image = models.ImageField(upload_to='images')

