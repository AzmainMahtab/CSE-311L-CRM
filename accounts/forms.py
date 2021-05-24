from django.forms import ModelForm, fields
from .models import Customer, Product, Order
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


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


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']