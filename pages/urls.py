from django.urls import path
from .views import HomePageView, ContactView

app_name = 'pages'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home')
]