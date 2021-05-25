from django.db import models
from django.db.models.expressions import OrderBy
from django.shortcuts import redirect, render
from .forms import CustomerForm, ProductForm, OrderForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from .filters import OrderFilter
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from .models import *

# Create your views here.

@login_required(login_url='login')
@admin_only
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products (request):
    if request.method == 'GET':
        form = ProductForm(request.POST)
        products = Product.objects.all()
        return render(request,"accounts/products.html", {'form': form, 'products': products})
    else:
        form = ProductForm(request.POST)
        form.save()
        return redirect('products')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers (request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        form = CustomerForm(request.POST)
        return render(request,"accounts/customers.html",{'form': form, 'customers': customers})

    else:
        form = CustomerForm(request.POST)
        form.save()
        return redirect('customers')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_order (request):
    if request.method == 'GET':
        form = OrderForm(request.POST)
        return render(request, 'accounts/add_order.html', {'form': form})
    else:
        form = OrderForm(request.POST)
        form.save()
        return redirect('home')


        ##### UPDATE FUCNTIONS ARE HERE #####


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def remove_order(request, pk):
    order = Order.objects.get(id=pk)
    context = {'order': order}

    if request.method == 'POST':
        order = Order.objects.get(id=pk)
        order.delete()
        return redirect('home')

    return render(request, 'accounts/remove_order.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def remove_product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}

    if request.method == 'POST':
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect('products')

    return render(request, 'accounts/remove_product.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def remove_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    context = {'customer': customer}

    if request.method == 'POST':
        customer = Customer.objects.get(id=pk)
        customer.delete()
        return redirect('customers')

    return render(request, 'accounts/remove_customer.html', context)

##### Authentications #####
@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,"Username or password is incorrect")
            return redirect('login')

    return render(request, 'accounts/login.html')


@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'account was created successfuly')

            return redirect('login')

    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

def userPage(request):
    return render(request, 'accounts/user.html')