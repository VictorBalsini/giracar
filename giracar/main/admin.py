from django.contrib import admin
from .models import CarRequest

@admin.register(CarRequest)
class CarRequestAdmin(admin.ModelAdmin):
    list_display = (
        'make', 'model', 'year', 
        'total_price', 'monthly_payment', 
        'contact', 'created_at'
    )
    list_filter = ('make', 'year', 'created_at')
    search_fields = ('make', 'model', 'contact', 'details')
    ordering = ('-created_at',)
