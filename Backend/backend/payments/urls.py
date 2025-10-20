from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('pay/pesapal/', views.pesapal_payment, name='pesapal_payment'),
    path('pay/mtn/', views.mtn_momo_payment, name='mtn_momo_payment'),
    path('pay/airtel/', views.airtel_money_payment, name='airtel_money_payment'),
]
