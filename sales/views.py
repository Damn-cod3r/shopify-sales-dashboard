# views.py
from django.shortcuts import render
from .models import Sale

def daily_sales_view(request):
    sales = Sale.objects.all().order_by('date')
    return render(request, 'dashboard.html', {'sales': sales})
