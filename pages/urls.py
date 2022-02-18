from django.urls import path
from .views import HomePageView, ContactView, AboutView

app_name = 'pages'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home')
]