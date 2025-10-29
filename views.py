from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import requests
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
@require_http_methods(["POST"])
def pay_mtn(request):
    try:
        data = json.loads(request.body)
        logger.info(f"MTN Payment request: {data}")
        
        # Validate required fields
        required_fields = ['amount', 'name', 'email', 'phone', 'mobile_number']
        for field in required_fields:
            if field not in data or not data[field]:
                return JsonResponse({
                    'success': False,
                    'error': f'Missing required field: {field}'
                }, status=400)
        
        # Simulate MTN Mobile Money payment processing
        # In production, you would integrate with MTN API here
        
        return JsonResponse({
            'success': True,
            'message': 'MTN Mobile Money payment initiated successfully',
            'transaction_id': f"MTN_{data['mobile_number']}_{int(time.time())}",
            'instructions': 'Please check your phone for Mobile Money prompt'
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        logger.error(f"MTN Payment error: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': f'Payment processing failed: {str(e)}'
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def pay_airtel(request):
    try:
        data = json.loads(request.body)
        logger.info(f"Airtel Payment request: {data}")
        
        # Validate required fields
        required_fields = ['amount', 'name', 'email', 'phone', 'mobile_number']
        for field in required_fields:
            if field not in data or not data[field]:
                return JsonResponse({
                    'success': False,
                    'error': f'Missing required field: {field}'
                }, status=400)
        
        # Simulate Airtel Money payment processing
        return JsonResponse({
            'success': True,
            'message': 'Airtel Money payment initiated successfully',
            'transaction_id': f"AIRTEL_{data['mobile_number']}_{int(time.time())}",
            'instructions': 'Please check your phone for Airtel Money prompt'
        })
        
    except Exception as e:
        logger.error(f"Airtel Payment error: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': f'Payment processing failed: {str(e)}'
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def pay_pesapal(request):
    try:
        data = json.loads(request.body)
        logger.info(f"Pesapal Payment request: {data}")
        
        # Validate required fields
        required_fields = ['amount', 'name', 'email', 'phone']
        for field in required_fields:
            if field not in data or not data[field]:
                return JsonResponse({
                    'success': False,
                    'error': f'Missing required field: {field}'
                }, status=400)
        
        # For Pesapal, you would typically redirect to their payment page
        # This is a simulation - in production, implement actual Pesapal integration
        
        return JsonResponse({
            'success': True,
            'message': 'Pesapal payment initiated',
            'redirect_url': 'https://www.pesapal.com/demo',  # Replace with actual Pesapal URL
            'transaction_id': f"PESAPAL_{int(time.time())}"
        })
        
    except Exception as e:
        logger.error(f"Pesapal Payment error: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': f'Payment processing failed: {str(e)}'
        }, status=500)

# Health check endpoint
@require_http_methods(["GET"])
def api_health(request):
    return JsonResponse({
        'status': 'ok',
        'message': 'YuSmile Uganda API is running',
        'timestamp': time.time()
    })