from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import time

@csrf_exempt
def mtn_momo_payment(request):
    print("MTN payment endpoint hit!")
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            
            # Always return success for testing
            return JsonResponse({
                'success': True,
                'message': 'MTN Payment initiated successfully',
                'transaction_id': f"MTN_{int(time.time())}",
                'instructions': 'Check your phone for Mobile Money prompt'
            })
        except Exception as e:
            print("Error:", e)
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def pesapal_payment(request):
    print("Pesapal payment endpoint hit!")
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            
            return JsonResponse({
                'success': True, 
                'message': 'Pesapal payment initiated',
                'transaction_id': f"PESAPAL_{int(time.time())}",
                'redirect_url': 'https://www.pesapal.com/demo'
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def airtel_money_payment(request):
    print("Airtel payment endpoint hit!")
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            
            return JsonResponse({
                'success': True,
                'message': 'Airtel Money payment initiated',
                'transaction_id': f"AIRTEL_{int(time.time())}",
                'instructions': 'Check your phone for Airtel Money prompt'
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'error': 'Method not allowed'}, status=405)

# Simple health check
def api_health(request):
    return JsonResponse({'status': 'ok', 'message': 'API is working'})
