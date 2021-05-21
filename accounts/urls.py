from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customers/', views.customers,name="customers"),
    path('customer/<str:pk>', views.customer, name="customer"),
    path('add_order/', views.add_order, name="add_order"),
    path('update_order/<str:pk>', views.update_order, name="update_order"),
    path('update_product/<str:pk>', views.update_product, name="update_product"),
    path('update_customer/<str:pk>', views.update_customer, name="update_customer"),
    path('remove_order/<str:pk>', views.remove_order, name="remove_order"),
    path('remove_product/<str:pk>', views.remove_product, name="remove_product"),
    
]
