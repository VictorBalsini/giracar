from django.db import models

class CarRequest(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    monthly_payment = models.DecimalField(max_digits=12, decimal_places=2)
    details = models.TextField(blank=True)
    contact = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price_brl(self):
        return f"R$ {self.total_price:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    @property
    def monthly_payment_brl(self):
        return f"R$ {self.monthly_payment:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    
    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"