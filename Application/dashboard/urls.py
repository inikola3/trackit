from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('increment_sales/', views.increment_sales, name='increment_sales'),
    path('webhook/', views.webhook, name='webhook')

]