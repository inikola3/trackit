from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    classification = models.CharField(max_length=15)
    container = models.CharField(max_length=50)
    fragrance = models.CharField(max_length=50)
    wax_type = models.CharField(max_length=50)
    wick_size = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    in_stock = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    product_image = models.ImageField(upload_to='product_images/', default='product_images/product_default4.svg', blank=True)

    def __str__(self):
        return self.name

class Component(models.Model):
    OUNCE = "oz"
    POUND = "lbs"
    NONE = "Ct"
    UNIT_CHOICES = {
        OUNCE: "oz",
        POUND: "lbs",
        NONE: "ct"
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    unit = models.CharField(max_length=3, choices=UNIT_CHOICES, default=NONE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    component_image = models.ImageField(upload_to='product_images/', default='product_images/product_default4.svg', blank=True)
    
    def __str__(self):
        return self.name


