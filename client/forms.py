from django import forms
from .models import ProfileModel


class ProfileModelForm(forms.ModelForm):

    class Meta:
        model = ProfileModel
        exclude = ['user']
