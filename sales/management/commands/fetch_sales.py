import requests
from django.core.management.base import BaseCommand
from sales.models import Sale
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetch sales from Shopify and save them to the database'

    def handle(self, *args, **kwargs):
        API_KEY = '76a2fd77d2cc4b18943f412e0a1631fa'
        PASSWORD = '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'
        SHOP_NAME = 'sales-data'
        
        url = f"https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin/api/2023-01/orders.json"

        response = requests.get(url)
        orders = response.json().get('orders', [])

        for order_data in orders:
            order_date = datetime.strptime(order_data['created_at'], '%Y-%m-%dT%H:%M:%S%z').date()
            total_price = order_data['total_price']
            sale, created = Sale.objects.update_or_create(
                date=order_date,
                defaults={'total_price': total_price}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Sale for {sale.date} created"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Sale for {sale.date} updated"))

        self.stdout.write(self.style.SUCCESS('Finished fetching sales'))