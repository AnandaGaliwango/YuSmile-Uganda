import json
import requests
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from dotenv import load_dotenv

load_dotenv()

# --------------------------
# CONTACT FORM (Email)
# --------------------------
@csrf_exempt
def contact_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        send_mail(
            subject=f"New Contact from {name}",
            message=message,
            from_email=email,
            recipient_list=["isaaqssegirinya@gmail.com"],
            fail_silently=False,
        )

        return JsonResponse({"status": "success", "message": "Email sent successfully!"})
    return JsonResponse({"error": "Invalid request"}, status=400)


# --------------------------
# PESAPAL PAYMENT
# --------------------------
@csrf_exempt
def pesapal_payment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        amount = data.get("amount")
        email = data.get("email")

        key = os.getenv("PESAPAL_KEY")
        secret = os.getenv("PESAPAL_SECRET")

        # Step 1: Get access token
        token_url = "https://pay.pesapal.com/v3/api/Auth/RequestToken"
        token_res = requests.post(token_url, json={"consumer_key": key, "consumer_secret": secret})
        access_token = token_res.json().get("token")

        # Step 2: Submit order request
        order_url = "https://pay.pesapal.com/v3/api/Transactions/SubmitOrderRequest"
        order_data = {
            "id": "ORDER001",
            "currency": "UGX",
            "amount": amount,
            "description": "Website Payment",
            "callback_url": "https://yourwebsite.com/payment/callback",
            "notification_id": "",
            "branch": "Online",
            "billing_address": {
                "email_address": email,
                "phone_number": "",
                "country_code": "UG",
                "first_name": "Customer",
                "last_name": "",
            },
        }

        headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
        order_res = requests.post(order_url, headers=headers, json=order_data)
        return JsonResponse(order_res.json())
    return JsonResponse({"error": "Invalid request"}, status=400)


# --------------------------
# MTN MOMO PAYMENT
# --------------------------
@csrf_exempt
def mtn_momo_payment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        amount = data.get("amount")
        phone = data.get("phone")

        sub_key = os.getenv("MTN_MOMO_SUBSCRIPTION_KEY")
        user_id = os.getenv("MTN_MOMO_USER_ID")

        # Step 1: Request access token
        token_url = "https://sandbox.momodeveloper.mtn.com/collection/token/"
        headers = {
            "Ocp-Apim-Subscription-Key": sub_key,
            "Authorization": f"Basic {user_id}"
        }
        token_res = requests.post(token_url, headers=headers)
        access_token = token_res.json().get("access_token")

        # Step 2: Create payment request
        pay_url = "https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "X-Reference-Id": "REQ12345",
            "X-Target-Environment": "sandbox",
            "Ocp-Apim-Subscription-Key": sub_key,
            "Content-Type": "application/json"
        }
        pay_data = {
            "amount": amount,
            "currency": "UGX",
            "externalId": "123456",
            "payer": {"partyIdType": "MSISDN", "partyId": phone},
            "payerMessage": "Website payment",
            "payeeNote": "Thanks for using our service"
        }
        pay_res = requests.post(pay_url, headers=headers, json=pay_data)

        return JsonResponse({"status": "pending", "message": "MTN MoMo payment initiated", "details": pay_res.text})
    return JsonResponse({"error": "Invalid request"}, status=400)


# --------------------------
# AIRTEL MONEY PAYMENT
# --------------------------
@csrf_exempt
def airtel_money_payment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        amount = data.get("amount")
        phone = data.get("phone")

        client_id = os.getenv("AIRTEL_CLIENT_ID")
        client_secret = os.getenv("AIRTEL_CLIENT_SECRET")

        # Step 1: Get token
        token_url = "https://openapi.airtel.africa/auth/oauth2/token"
        payload = {"client_id": client_id, "client_secret": client_secret, "grant_type": "client_credentials"}
        token_res = requests.post(token_url, json=payload)
        access_token = token_res.json().get("access_token")

        # Step 2: Initiate payment
        pay_url = "https://openapi.airtel.africa/merchant/v1/payments/"
        headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
        pay_data = {
            "reference": "TXN001",
            "subscriber": {"country": "UG", "currency": "UGX", "msisdn": phone},
            "transaction": {"amount": amount, "country": "UG", "currency": "UGX"},
        }

        pay_res = requests.post(pay_url, headers=headers, json=pay_data)
        return JsonResponse(pay_res.json())
    return JsonResponse({"error": "Invalid request"}, status=400)
