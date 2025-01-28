from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('add_product/', views.add_product, name='add_product'),    
    path('<str:name>/<int:id>/', views.product_page, name='product_page'),   
    path('components/', views.components, name = 'components'),
    path('add_component/', views.add_component, name='add_component'), 
    path('components/<str:name>/<int:id>/', views.component_page, name='component_page'),
    path('recipes/', views.create_recipe, name = 'create_recipe'),
]