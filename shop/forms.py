from django import forms
from .models import ColorModel


class ColorModelForm(forms.ModelForm):
    code = forms.CharField(max_length=7, widget=forms.TextInput(attrs={'type': 'color'}),)

    class Meta:
        model = ColorModel
        fields = '__all__'
