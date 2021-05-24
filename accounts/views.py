from django.db import models
from django.db.models.expressions import OrderBy
from django.shortcuts import redirect, render
from .forms import CustomerForm, ProductForm, OrderForm
from .filters import OrderFilter
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

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'customer': customer,
        'orders': orders,
        'myFilter': myFilter,
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


        ##### UPDATE FUCNTIONS ARE HERE #####

def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        order = Order.objects.get(id=pk)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    

    return render(request, 'accounts/update_order.html', {'form': form, 'order': order})

def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        product = Product.objects.get(id=pk)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    

    return render(request, 'accounts/update_product.html', {'form': form, 'product': product})

def update_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        customer = Customer.objects.get(id=pk)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')
    

    return render(request, 'accounts/update_customer.html', {'form': form, 'customer': customer})

     ##### DELETE FUNCTIONS ARE HERE #####

def remove_order(request, pk):
    order = Order.objects.get(id=pk)
    context = {'order': order}

    if request.method == 'POST':
        order = Order.objects.get(id=pk)
        order.delete()
        return redirect('home')

    return render(request, 'accounts/remove_order.html', context)

def remove_product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}

    if request.method == 'POST':
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect('products')

    return render(request, 'accounts/remove_product.html', context)

def remove_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    context = {'customer': customer}

    if request.method == 'POST':
        customer = Customer.objects.get(id=pk)
        customer.delete()
        return redirect('customers')

    return render(request, 'accounts/remove_customer.html', context)