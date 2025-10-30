from django.urls import path
from . import views

urlpatterns = [
    # Contact form
    path('contact/', views.contact_view, name='contact'),

    # Payments
    path('pay/pesapal/', views.pesapal_payment, name='pesapal_payment'),
    path('pay/mtn/', views.mtn_momo_payment, name='mtn_momo_payment'),
    path('pay/airtel/', views.airtel_money_payment, name='airtel_money_payment'),  # Uncommented

    # Payment callbacks / IPNs
    path('pesapal-callback/', views.pesapal_callback, name='pesapal_callback'),
    path('mtn-momo-callback/', views.mtn_momo_callback, name='mtn_momo_callback'),

    # Health check
    path('health/', views.api_health, name='api_health'),
    path('', views.api_health, name='api_root'),
]
