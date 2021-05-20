from django.db import models
from django.db.models.expressions import OrderBy
from django.shortcuts import redirect, render
from .forms import CustomerForm, ProductForm
from .models import Customer, Product

# Create your views here.

def home (request):
    return render(request,"accounts/index.html", context={})

def products (request):
    if request.method == 'GET':
        form = ProductForm(request.POST)
        products = Product.objects.all()
        return render(request,"accounts/products.html", {'form': form, 'products': products})
    else:
        form = ProductForm(request.POST)
        form.save()
        return redirect('products')
def customer (request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        form = CustomerForm(request.POST)
        return render(request,"accounts/customer.html",{'form': form, 'customers': customers})

    else:
        form = CustomerForm(request.POST)
        form.save()
        return redirect('customer')