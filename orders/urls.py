from django.urls import path

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout')
]