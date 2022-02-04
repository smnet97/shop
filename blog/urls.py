from django.urls import path
from .views import BlogListView

app_name = 'blogs'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list')
]