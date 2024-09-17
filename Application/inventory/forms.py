from django import forms
from . import models
from django.forms.widgets import ClearableFileInput


class AddProduct(forms.ModelForm):
    
    class Meta:
        model = models.Product
        fields = ['name', 'classification', 
                  'container', 'fragrance', 
                  'wax_type', 'wick_size', 
                  'price', 'quantity', 'in_stock', 'product_image'
                  ]
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),#, 'style' : 'width:100%;''float:left;'}),
            'classification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Class'}),#, 'style' : 'width:50%;' 'float:right;'}),
            'container': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Container Type'}),
            'fragrance': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fragrace Name'}),
            'wax_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wax Type'}),
            'wick_size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wick Type'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
            'in_stock': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style' : 'transform:translateY(12px);'}),
        }

class Component(forms.ModelForm):
    class Meta:
        model = models.Component
        fields = ['name', 'unit', 
                  'quantity', 'price', 'component_image'
                ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control-components', 'placeholder': 'Name'}),#, 'style' : 'width:100%;''float:left;'}),
            'unit': forms.Select(attrs={'class': 'form-dropdown'}),#, 'style' : 'width:50%;' 'float:right;'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control-components', 'placeholder': 'Quantity' }),
            'price': forms.TextInput(attrs={'class': 'form-control-components', 'placeholder': 'Price per unit'}),            
        }