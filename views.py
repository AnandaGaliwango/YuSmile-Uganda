import json
import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@csrf_exempt
@require_http_methods(["POST"])
def mtn_momo_payment(request):
    """Handle MTN Mobile Money payments"""
    try:
        data = json.loads(request.body)
        print(f"🎯 MTN Mobile Money Payment Request:")
        print(f"   Name: {data.get('name')}")
        print(f"   Email: {data.get('email')}")
        print(f"   Phone: {data.get('phone')}")
        print(f"   Mobile: {data.get('mobile_number')}")
        print(f"   Amount: UGX {data.get('amount')}")
        
        # Validate required fields
        required_fields = ['amount', 'name', 'email', 'phone', 'mobile_number']
        for field in required_fields:
            if field not in data or not data[field]:
                return JsonResponse({
                    'success': False,
                    'error': f'Missing required field: {field}'
                }, status=400)
        
        # Simulate MTN Mobile Money processing
        transaction_id = f"MTN_{data['mobile_number']}_{int(time.time())}"
        
        print(f"✅ MTN Payment processed successfully: {transaction_id}")
        
        return JsonResponse({
            'success': True,
            'message': 'MTN Mobile Money payment initiated successfully',
            'transaction_id': transaction_id,
            'instructions': f'Please check your phone {data["mobile_number"]} for Mobile Money prompt'
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        print(f"❌ MTN Payment error: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': f'Payment processing failed: {str(e)}'
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def pesapal_payment(request):
    """Handle Pesapal payments"""
    try:
        data = json.loads(request.body)
        print(f"🎯 Pesapal Payment Request:")
        print(f"   Name: {data.get('name')}")
        print(f"   Email: {data.get('email')}")
        print(f"   Phone: {data.get('phone')}")
        print(f"   Amount: UGX {data.get('amount')}")
        
        # Validate required fields
        required_fields = ['amount', 'name', 'email', 'phone']
        for field in required_fields:
            if field not in data or not data[field]:
                return JsonResponse({
                    'success': False,
                    'error': f'Missing required field: {field}'
                }, status=400)
        
        # Simulate Pesapal processing
        transaction_id = f"PESAPAL_{int(time.time())}"
        
        print(f"✅ Pesapal Payment processed successfully: {transaction_id}")
        
        return JsonResponse({
            'success': True,
            'message': 'Pesapal payment initiated successfully',
            'transaction_id': transaction_id,
            'redirect_url': 'https://www.pesapal.com/demo',  # Replace with actual URL
        })
        
    except Exception as e:
        print(f"❌ Pesapal Payment error: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': f'Payment processing failed: {str(e)}'
        }, status=500)

# Add Airtel Money endpoint since frontend expects it
@csrf_exempt
@require_http_methods(["POST"])
def airtel_money_payment(request):
    """Handle Airtel Money payments"""
    try:
        data = json.loads(request.body)
        print(f"🎯 Airtel Money Payment Request:")
        print(f"   Name: {data.get('name')}")
        print(f"   Email: {data.get('email')}")
        print(f"   Phone: {data.get('phone')}")
        print(f"   Mobile: {data.get('mobile_number')}")
        print(f"   Amount: UGX {data.get('amount')}")
        
        # Validate required fields
        required_fields = ['amount', 'name', 'email', 'phone', 'mobile_number']
        for field in required_fields:
            if field not in data or not data[field]:
                return JsonResponse({
                    'success': False,
                    'error': f'Missing required field: {field}'
                }, status=400)
        
        # Simulate Airtel Money processing
        transaction_id = f"AIRTEL_{data['mobile_number']}_{int(time.time())}"
        
        print(f"✅ Airtel Money Payment processed successfully: {transaction_id}")
        
        return JsonResponse({
            'success': True,
            'message': 'Airtel Money payment initiated successfully',
            'transaction_id': transaction_id,
            'instructions': f'Please check your phone {data["mobile_number"]} for Airtel Money prompt'
        })
        
    except Exception as e:
        print(f"❌ Airtel Money Payment error: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': f'Payment processing failed: {str(e)}'
        }, status=500)

# Add health check endpoint
@require_http_methods(["GET"])
def api_health(request):
    return JsonResponse({
        'status': 'ok',
        'message': 'YuSmile Uganda Payments API is running',
        'timestamp': time.time(),
        'endpoints': {
            'MTN Mobile Money': '/api/pay/mtn/',
            'Airtel Money': '/api/pay/airtel/',
            'Pesapal': '/api/pay/pesapal/'
        }
    })

# Your existing callback functions
def pesapal_callback(request):
    # Your existing implementation
    return JsonResponse({'status': 'callback received'})

def mtn_momo_callback(request):
    # Your existing implementation
    return JsonResponse({'status': 'callback received'})
