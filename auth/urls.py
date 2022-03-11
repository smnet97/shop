from django.urls import path, include
from .views import reset_password
urlpatterns = [
    path('password/change/done/', reset_password),
    path('', include('registration.backends.default.urls'))
]