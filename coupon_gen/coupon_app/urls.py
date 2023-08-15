from django.urls import path
from . import views

urlpatterns = [
    path('generate-coupon/', views.generate_coupon, name='generate_coupon'),
    path('check-coupon/', views.check_coupon, name='check_coupon'),
]
