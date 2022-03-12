from django.shortcuts import render
from django.views.generic import CreateView

from shop.models import ProductModel
from .forms import OrderModelForm


class CheckoutView(CreateView):
    template_name = 'main/checkout.html'
    form_class = OrderModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', [])
        context['products'] = ProductModel.get_cart_info(cart)

        if hasattr(self.request.user.profiles, 'profiles'):
            context['profile'] = self.request.user.profiles

        return context

