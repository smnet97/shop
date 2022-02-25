from django.db.models.signals import pre_save
from django.dispatch import receiver

from shop.models import ProductModel


@receiver(pre_save, sender=ProductModel)
def real_price_get(sender, instance, *args, **kwargs):

    if instance.is_discount():
        print((100 - instance.discount) / 100 * instance.price)
        instance.real_price = (100 - instance.discount) / 100 * instance.price
    else:
        instance.real_price = instance.price