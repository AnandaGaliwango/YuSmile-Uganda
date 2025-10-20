# payments/models.py
from django.db import models

class Payment(models.Model):
    PAYMENT_CHOICES = [
        ('pesapal', 'Pesapal'),
        ('mtn', 'MTN Mobile Money'),
        ('airtel', 'Airtel Money'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ]

    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.payment_method} - {self.phone_number} - {self.amount}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
