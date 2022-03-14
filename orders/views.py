from django.db.models import Sum
from django.shortcuts import render, reverse, redirect
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from shop.models import ProductModel
from .forms import OrderModelForm


class CheckoutView(CreateView):
    template_name = 'main/checkout.html'
    form_class = OrderModelForm

    def get_success_url(self):
        return reverse('orders:history')

    def form_valid(self, form):
        cart = self.request.session.get('cart', [])
        products = ProductModel.get_cart_info(cart)

        form.instance.user = self.request.user
        form.instance.price = products.aggregate(
            Sum('real_price')
        )['real_price__sum']

        order = form.save()
        order.products.set(products)

        self.request.session['cart'] = []

        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', [])
        context['products'] = ProductModel.get_cart_info(cart)

        if hasattr(self.request.user, 'profiles'):
            context['profile'] = self.request.user.profiles

        return context


class OrderHistoryListView(LoginRequiredMixin, ListView):
    template_name = 'main/history.html'

    def get_queryset(self):
        return self.request.user.orders.all()

