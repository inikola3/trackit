from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from inventory.models import Product, Component, Recipe, RecipeMaterials
from .models import DailySales
import datetime
from django.http import JsonResponse
import json
import jwt
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        try:
            # Decode the JWT from the request body
            token = request.body.decode('utf-8')
            data = jwt.decode(token, options={"verify_signature": False})  # Decode without verification

            # Debug statement to check if data is received
            print("Received data:", data)

            order = data.get('order')
            order_value = data.get('current_total_price')
            if order:               
                today = datetime.date.today()
                user = User.objects.get(id=1)
                sales_record, created = DailySales.objects.get_or_create(date=today, user=user)
                sales_record.sales_count += 1
                sales_record.save()
                return JsonResponse({'status': 'success'})
            else:
                print("Order not found in data")
        except Exception as e:
            print("Exception:", str(e))
    
    return JsonResponse({'status': 'failed'}, status=400)

#Test sales data 
def increment_sales(request):
    today = datetime.date.today()
    sales_record, created = DailySales.objects.get_or_create(date=today, user=request.user)
    sales_record.sales_count += 1
    sales_record.order_value += 20
    sales_record.save()
    return HttpResponse('Sales count and order value updated')



@login_required(login_url="/users/login/")
def dashboard(request):
   # Stock alerts
   out_of_stock_products = Product.objects.filter(in_stock=True, quantity=0,user=request.user).count()
   near_out_of_stock_products = Product.objects.filter(in_stock=True, quantity__range=(1,3),user=request.user).count()
   out_of_stock_components = Component.objects.filter(quantity=0, user=request.user).count()
   near_out_of_stock_components = Component.objects.filter(quantity__range=(1,3),user=request.user).count()

   # Cost of goods stats
#    components = Component.objects.filter(user=request.user)
#    if components.count() == 0:
#        data = {
#         'labels': ['No data to show'],
#         'prices': [1.00]  
#        }
#    else:
#        data = {
#                 'labels': [component.name for component in components],
#                 'prices': [float(component.price) for component in components]  
#        }
   
#    cog_total = 0
#    for component in components:
#      cog_total += component.price
   
   today = datetime.date.today()
   sales_record = DailySales.objects.filter(date=today, user=request.user).first()
   if sales_record:
       sales_count = sales_record.sales_count
       sales_today_total = sales_record.order_value
   else:
       sales_count = 0
       sales_today_total = 0
#    sales_count = sales_record.sales_count if sales_record else 0
    
   daily_goal = 10 
   all_time_sales = DailySales.objects.filter(user=request.user)
   
   all_time_sales_count = 0
   all_time_sales_value = 0
   for sale in all_time_sales:
       all_time_sales_count += sale.sales_count
       all_time_sales_value += sale.order_value
    
   all_sales_data = {
      'dates' : [str(sale.date) for sale in all_time_sales],
      'sales' : [sale.sales_count for sale in all_time_sales]
   }
   all_sales_value = {
      'dates' : [str(sale.date) for sale in all_time_sales],
      'sales' : [sale.order_value for sale in all_time_sales]
   }
   
   total_orders_value = 0
   for sale in all_time_sales:
        total_orders_value += sale.order_value    
   
   if all_time_sales_count > 0:
        average_order_value = total_orders_value/all_time_sales_count
   else:
       average_order_value = 0.00 

   products = Product.objects.filter(user=request.user)
   
#    product = Product.objects.get(name='12oz Gardenia Tuberose')
#    print(product.id) 
   return render(request, 'dashboard/dashboard.html',
                 {'out_of_stock_products':out_of_stock_products,
                  'out_of_stock_components':out_of_stock_components,
                  'near_out_of_stock_products':near_out_of_stock_products, 
                  'near_out_of_stock_components':near_out_of_stock_components,
                #   'data':data,
                #   'cog_total':cog_total,
                  'sales_count': sales_count,
                  'daily_goal': daily_goal,
                  'all_sales_data':all_sales_data,
                  'all_time_sales_count':all_time_sales_count,
                  'average_order_value':round(average_order_value,2), 
                  'sales_today_total' : sales_today_total,
                  'all_sales_value' : all_sales_value,
                  'all_time_sales_value':all_time_sales_value,
                  'products':products
                  })


def get_cog(request, product_id):
    product = Product.objects.get(id=product_id)
    recipe = product.recipe
    materials = RecipeMaterials.objects.filter(recipe=recipe)
    if materials.count() == 0:
       data = {
        'labels': ['Missing Data'],
        'prices': [1.00]  
       }
    else:
        data = {
            'labels':[material.material.name for material in materials],
            'prices':[float(material.material.price) * float(material.quantity) for material in materials] 
        }
    return JsonResponse(data)