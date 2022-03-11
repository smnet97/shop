from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView
from .forms import ProfileModelForm
from .models import ProfileModel
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'main/profile.html'
    form_class = ProfileModelForm

    def get_success_url(self):
        return reverse('profile:home')

    def get_object(self, queryset=None):
        profile, created = ProfileModel.objects.get_or_create(user=self.request.user)
        return profile

