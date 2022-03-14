from django.contrib.auth import get_user_model
from django.db import models
from shop.models import ProductModel
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class OrderModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='orders')
    products = models.ManyToManyField(ProductModel)
    price = models.FloatField()

    first_name = models.CharField(max_length=30, verbose_name=_('first name'))
    last_name = models.CharField(max_length=30, verbose_name=_('last name'))
    country = models.CharField(max_length=30, verbose_name=_('country'))
    address1 = models.CharField(max_length=255, verbose_name=_('address'))
    address2 = models.CharField(max_length=255, verbose_name=_('address'), null=True, blank=True)
    city = models.CharField(max_length=30, verbose_name=_('city'))
    state = models.CharField(max_length=30, verbose_name=_('state'))
    zip_code = models.CharField(max_length=30, verbose_name=_('zip code'))
    phone = models.CharField(max_length=13, verbose_name=_('phone'))
    email = models.EmailField(verbose_name=_('email'))

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.price}'

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'


