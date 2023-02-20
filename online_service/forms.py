from django import forms
from .models import Product

# Пример формы для добавления продукта:
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']