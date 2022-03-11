from django.shortcuts import render
from django.views.generic import CreateView


class CheckoutView(CreateView):
    template_name = 'main/checkout.html'
