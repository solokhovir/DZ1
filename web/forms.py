from django import forms
from .models import Recognize


class Form(forms.ModelForm):
    class Meta:
        model = Recognize
        fields = ('image',)

