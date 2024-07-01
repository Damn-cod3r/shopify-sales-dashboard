from django.urls import path, include
from .views import daily_sales_view

urlpatterns = [
    path('sales/', daily_sales_view, name='dashboard'),
    
]
