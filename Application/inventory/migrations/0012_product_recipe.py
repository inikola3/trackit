# Generated by Django 5.0.6 on 2024-11-03 03:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_recipe_recipematerials'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='inventory.recipe'),
        ),
    ]
