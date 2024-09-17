from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class DailySales(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(unique=True)
    sales_count = models.PositiveIntegerField(default=0)
    order_value = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Sales on {self.date}: {self.sales_count}"