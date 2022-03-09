from django.contrib import admin

from .models import ProfileModel


@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'country']
    list_display_links = ['first_name', 'last_name', 'country']
    search_fields = ['first_name', 'last_name', 'country']

