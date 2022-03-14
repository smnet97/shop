from django.contrib import admin

from orders.models import OrderModel


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'price', 'created_at']
    list_display_links = ['id', 'user', 'price', 'created_at']

