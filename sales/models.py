from django.db import models

class Sale(models.Model):
    date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.total_price}"
