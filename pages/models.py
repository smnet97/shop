from django.db import models
from django.utils.translation import gettext_lazy as _


class BannerModel(models.Model):
    title = models.CharField(max_length=64, verbose_name=_('title'))
    collection = models.CharField(max_length=54, verbose_name=_('collection'))
    description = models.TextField(verbose_name=_("description"))
    banner = models.ImageField(upload_to='banners', verbose_name=_('banner'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('banner')
        verbose_name_plural = _('banners')


class ContactModel(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at')
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'