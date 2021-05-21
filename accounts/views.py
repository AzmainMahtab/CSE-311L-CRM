from django.db import models
from django.db.models.expressions import OrderBy
from django.shortcuts import redirect, render
from .forms import CustomerForm, ProductForm, OrderForm
from .models import *

# Create your views here.

def home (request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_order = orders.count()

    pending = 0
    delivered = 0

    for ordr in orders:
        if ordr.status == "Pending":
            pending = pending + 1
        if ordr.status == "Delivered":
            delivered = delivered + 1
    

    context = {
        'customers': customers,
        'orders': orders,
        'total_order': total_order,
        'delivered': delivered,
        'pending': pending,
    }

    return render(request,"accounts/index.html", context)

def products (request):
    if request.method == 'GET':
        form = ProductForm(request.POST)
        products = Product.objects.all()
        return render(request,"accounts/products.html", {'form': form, 'products': products})
    else:
        form = ProductForm(request.POST)
        form.save()
        return redirect('products')

def customers (request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        form = CustomerForm(request.POST)
        return render(request,"accounts/customers.html",{'form': form, 'customers': customers})

    else:
        form = CustomerForm(request.POST)
        form.save()
        return redirect('customers')

def customer (request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()

    context = {
        'customer': customer,
        'orders': orders,
        }
    return render(request,'accounts/customer.html', context)

def add_order (request):
    if request.method == 'GET':
        form = OrderForm(request.POST)
        return render(request, 'accounts/add_order.html', {'form': form})
    else:
        form = OrderForm(request.POST)
        form.save()
        return redirect('home')