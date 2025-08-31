from django.contrib import admin
from .models import CarRequest

@admin.register(CarRequest)
class CarRequestAdmin(admin.ModelAdmin):
    list_display = (
        'make', 'model', 'year',  
        'details', 'local', 
        'contact', 'created_at'
    )
    list_filter = ('make', 'year', 'local')
    search_fields = ('make', 'model', 'local')
    ordering = ('make',)
