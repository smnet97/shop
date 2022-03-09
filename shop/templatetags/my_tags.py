from django import template
from django.db.models import Sum

from product.models import WishListModel
from shop.models import ProductModel

register = template.Library()

@register.simple_tag
def get_cart_info(request):
    cart = request.session.get('cart', [])
    print(cart)
    if not cart:
        return 0, 0.0

    return len(cart), ProductModel.get_cart_info(cart).aggregate(Sum('real_price'))['real_price__sum']

@register.simple_tag
def get_current_price(request, x):
    t = request.GET.get('price')
    if t:
        return t.split(';')[x] # [ 23, 45]
    else:
        return 'null'

@register.filter
def is_wishlist(product, user):
    return WishListModel.objects.filter(user=user, product=product).exists()

@register.filter
def is_cart(request, product):
    return product.pk in request.session.get('cart', [])