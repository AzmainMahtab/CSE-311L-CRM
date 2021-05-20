from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    email = models.EmailField()