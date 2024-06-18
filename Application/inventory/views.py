from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Component
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

@login_required(login_url="/users/login/")
def inventory(request):
    if request.method == 'POST':
        selected_products = request.POST.getlist('selected_products')
        for product_id in selected_products:
            product = get_object_or_404(Product, id=product_id, user=request.user)
            product.delete()
        return redirect('/inventory')
    
    products = Product.objects.filter(user=request.user)
    product_count = products.count()
    
    out_of_stock = Product.objects.filter(quantity=0,user=request.user).count()
    
    quantity_total = 0
    for product in Product.objects.filter(user=request.user):
        quantity_total += product.quantity
    
    total_value = 0
    for product in Product.objects.filter(user=request.user):
        total_value += product.price * product.quantity

    return render(request, "inventory/inventory.html", { 
        'products':products, 
        'product_count': product_count,
        'out_of_stock' : out_of_stock,
        'quantity_total':quantity_total,
        'total_value':total_value
    })

@login_required(login_url="/users/login/")
def add_product(request):
    if request.method == 'POST':
        form = forms.AddProduct(request.POST, request.FILES)
        if form.is_valid():
            newproduct = form.save(commit=False)
            newproduct.user = request.user
            newproduct.save() 
            return redirect('inventory:inventory')
    else:    
        form = forms.AddProduct
    return render(request, 'inventory/add_product.html', { 'form':form })

@login_required(login_url="/users/login/")
def product_page(request, name, id):
    product = get_object_or_404(Product, name=name, id=id, user=request.user)
    if request.method == 'POST':
        print(request.FILES)
        form = forms.AddProduct(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('inventory:inventory')
    else:
        form = forms.AddProduct(instance=product)
    return render(request, 'inventory/product_page.html', {'form': form, 'product': product})

login_required(login_url="/users/login/")
def components(request):
    component = Component.objects.filter(user=request.user)
    if request.method == 'POST':
        selected_components = request.POST.getlist('selected_components')
        for component_id in selected_components:
            component = get_object_or_404(Component, id=component_id, user=request.user)
            component.delete()
        return redirect('inventory:components')
    
    component_count = component.count()
    out_of_stock = Component.objects.filter(quantity = 0, user=request.user).count()
    
    return render(request, "inventory/components.html", 
                  { 'components' : component,
                    'component_count' : component_count,
                    'out_of_stock' : out_of_stock,
                   })


@login_required(login_url="/users/login/")
def add_component(request):
    if request.method == 'POST':
        form = forms.Component(request.POST, request.FILES)
        if form.is_valid():
            newcomponent = form.save(commit=False)
            newcomponent.user = request.user
            newcomponent.save() 
            return redirect('inventory:components')
    else:    
        form = forms.Component
    return render(request, 'inventory/add_component.html', { 'form':form })


@login_required(login_url="/users/login/")
def component_page(request, name, id):
    component = get_object_or_404(Component, name=name, id=id, user=request.user)
    if request.method == 'POST':
        form = forms.Component(request.POST, request.FILES, instance=component)
        if form.is_valid():
            form.save()
            return redirect('inventory:components')
    else:
        form = forms.Component(instance=component)
    return render(request, 'inventory/component_page.html', {'form': form, 'component': component})