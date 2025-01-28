from django import forms
from . import models
from django.forms.widgets import ClearableFileInput
from .models import Recipe, RecipeMaterials
from django.forms import inlineformset_factory

class AddProduct(forms.ModelForm):
    
    class Meta:
        model = models.Product
        fields = ['name', 'classification', 
                  'container', 'fragrance', 
                  'wax_type', 'wick_size', 
                  'price', 'quantity', 'in_stock', 'product_image', 'recipe'
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
            'recipe':forms.Select(attrs={'class':'form-control', 'style':'transform:translateY(6px);', 'empty_label':'Select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['recipe'].empty_label = 'Select a Recipe'

class Component(forms.ModelForm):
    class Meta:
        model = models.Component
        fields = ['name', 'unit', 
                  'quantity', 'price', 'component_image'
                ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),#, 'style' : 'width:100%;''float:left;'}),
            'unit': forms.Select(attrs={'class': 'form-dropdown'}),#, 'style' : 'width:50%;' 'float:right;'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quantity' }),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price per unit'}),            
        }


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description']
        widgets = {
            'name':forms.TextInput(attrs={'class':'modal-field', 'label':'Name'}),
            'description':forms.TextInput(attrs={'class':'modal-field'})
        }

class RecipeMaterialForm(forms.ModelForm):
    class Meta:
        model = RecipeMaterials
        fields = ['material', 'quantity']
        widgets = {
            'material':forms.Select(attrs={'class':'modal-field dropdown'}),
            'quantity':forms.NumberInput(attrs={'class':'modal-field quantity'})
        }

RecipeMaterialFormSet = inlineformset_factory(Recipe, RecipeMaterials, form=RecipeMaterialForm, extra=1, can_delete=False)