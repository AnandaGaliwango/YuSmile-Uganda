from django.urls import path
from . import views

urlpatterns = [
    # Contact form
    path('contact/', views.contact_view, name='contact'),

    # Payments
    path('pay/pesapal/', views.pesapal_payment, name='pesapal_payment'),
    path('pay/mtn/', views.mtn_momo_payment, name='mtn_momo_payment'),
    # path('pay/airtel/', views.airtel_money_payment, name='airtel_money_payment'),

    # Payment callbacks / IPNs
    path('pesapal-callback/', views.pesapal_callback, name='pesapal_callback'),
    path('mtn-momo-callback/', views.mtn_momo_callback, name='mtn_momo_callback'),
    # path('airtel-money-callback/', views.airtel_money_callback, name='airtel_money_callback'),
]
