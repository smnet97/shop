from django.contrib.auth import get_user_model
from django.db import models, IntegrityError
from django.utils.translation import gettext_lazy as _
from shop.models import ProductModel

UserModel = get_user_model()


class WishListModel(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        verbose_name=_('user'),
        related_name=_('wishlist')
    )
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        verbose_name=_('product'),
        related_name=_('wishlist')
    )

    def __str__(self):
        return self.user.get_full_name() + ' | ' + self.product.name

    @staticmethod
    def add_to_delete(user, product):
        try:
            WishListModel.objects.create(user=user, product=product)
        except IntegrityError:
            WishListModel.objects.all().filter(user=user, product=product).delete()

    class Meta:
        verbose_name = 'wishlist'
        verbose_name_plural = 'wishlists'
        unique_together = 'user', 'product',


