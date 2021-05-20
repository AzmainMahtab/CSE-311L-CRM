from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Order, Product, Customer

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Order,OrderAdmin)
