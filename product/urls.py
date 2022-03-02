from django.urls import path
from .views import update_wishlist, WishlistView

app_name = 'products'

urlpatterns = [
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('<int:pk>/wishlist/', update_wishlist, name='add_wishlist')
]