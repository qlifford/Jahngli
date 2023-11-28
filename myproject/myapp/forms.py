from django.core import validators
from django import forms
from .models import Product

class CreateProductForm(forms.ModelForm):
    name = forms.CharField(max_length=100)

    class Meta:
        model = Product
        fields = ['name',]