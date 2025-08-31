from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('comprar/', views.buy_car, name='comprar'),
    path('dashboard/', views.dashboard, name='dashboard'),    
    path('api/makes/', views.get_makes, name='get_makes'),
    path('api/models/<str:make>/', views.get_models, name='get_models'),
]
