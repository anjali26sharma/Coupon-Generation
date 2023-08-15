from django.shortcuts import render
from django.http import HttpRequest

from django.template import loader
from .logic import generate_coupon_code,is_valid_coupon
from django.http import JsonResponse

# Create your views here.

def hello(request):
    return render(request,'hello.html')

def generate_coupon(request):
    if request.method == 'POST':
        # Generate a coupon code
        coupon = generate_coupon_code()
        return render(request, 'coupon_generated.html', {'coupon': coupon})
    return render(request, 'generate_coupon.html')

def check_coupon(request):
    if request.method == 'POST':
        coupon_to_check = request.POST.get('coupon_to_check', '')
        if is_valid_coupon(coupon_to_check):
            return render(request, 'coupon_valid.html')
        else:
            return render(request, 'coupon_invalid.html')
    return render(request, 'check_coupon.html')