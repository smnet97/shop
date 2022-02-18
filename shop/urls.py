from django.urls import path
from .views import ShopView, ProductDetailView

app_name = 'shops'

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('<int:pk>/detail/', ProductDetailView.as_view(), name='product_detail')
]