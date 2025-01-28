from django.contrib import admin
from .models import Product, Component, Recipe, RecipeMaterials
# Register your models here.
admin.site.register(Product)
admin.site.register(Component)
admin.site.register(Recipe)
admin.site.register(RecipeMaterials)