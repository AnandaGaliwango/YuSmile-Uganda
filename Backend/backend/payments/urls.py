from django.urls import path
from . import views

urlpatterns = [
    path('pay/mtn/', views.mtn_momo_payment, name='mtn_momo_payment'),
    path('pay/pesapal/', views.pesapal_payment, name='pesapal_payment'),
    path('pay/airtel/', views.airtel_money_payment, name='airtel_money_payment'),
    path('health/', views.api_health, name='api_health'),
    path('', views.api_health, name='api_root'),
]
