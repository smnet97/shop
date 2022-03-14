from django.urls import path

from orders.views import CheckoutView, OrderHistoryListView

app_name = 'orders'

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('history/', OrderHistoryListView.as_view(), name='history')
]