from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Product, Customer

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
