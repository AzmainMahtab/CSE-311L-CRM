from django.forms import ModelForm, fields
from .models import Customer, Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email']