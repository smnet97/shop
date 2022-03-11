from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


def reset_password(request):
    messages.add_message(request, messages.INFO, _('Password changed successfully !'))
    return redirect(reverse('profile:home'))

# /profile/home/
