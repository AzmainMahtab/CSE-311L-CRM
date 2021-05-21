from django.forms import ModelForm, fields
from .models import Customer, Product, Order

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'status']