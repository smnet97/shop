from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, verbose_name=_('user'), related_name='profiles')
    first_name = models.CharField(max_length=30, verbose_name=_('first name'), null=True, blank=True)
    last_name = models.CharField(max_length=30, verbose_name=_('last name'), null=True, blank=True)
    country = models.CharField(max_length=30, verbose_name=_('country'), null=True, blank=True)
    address1 = models.CharField(max_length=255, verbose_name=_('address'), null=True, blank=True)
    address2 = models.CharField(max_length=255, verbose_name=_('address'), null=True, blank=True)
    city = models.CharField(max_length=30, verbose_name=_('city'), null=True, blank=True)
    state = models.CharField(max_length=30, verbose_name=_('state'), null=True, blank=True)
    zip_code = models.CharField(max_length=30, verbose_name=_('zip code'), null=True, blank=True)
    phone = models.CharField(max_length=13, verbose_name=_('phone'), null=True, blank=True)
    email = models.EmailField(verbose_name=_('email'), null=True, blank=True)
    #
    # def __str__(self):
    #     return self.first_name

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')