from django.shortcuts import render, redirect, get_object_or_404
from .models import WishListModel
from django.contrib.auth.decorators import login_required
from shop.models import ProductModel
from django.views.generic import ListView


class WishlistView(ListView):
    template_name = 'main/wishlist.html'

    def get_queryset(self):
        print(self.request.user.id)
        return ProductModel.objects.all().filter(wishlist__user_id=self.request.user.id)


@login_required
def update_wishlist(request, pk):
    product = get_object_or_404(ProductModel.objects.all().filter(id=pk))
    wishlist = WishListModel.add_to_delete(request.user, product)

    return redirect(request.GET.get('next', '/'))


def update_cart(request, pk):
    product = get_object_or_404(ProductModel.objects.all().filter(id=pk))
    cart = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)

    request.session['cart'] = cart

    return redirect(request.GET.get('next', '/'))


class CartListView(ListView):
    template_name = 'main/shopping_cart.html'

    def get_queryset(self):
        cart = self.request.session.get('cart', [])
        return ProductModel.get_cart_info(cart)