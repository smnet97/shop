from django.urls import path
from .views import BlogListView, BlogDetailView

app_name = 'blogs'

urlpatterns = [
    path('<int:pk>/post/', BlogDetailView.as_view(), name='blog_detail'),
    path('', BlogListView.as_view(), name='blog_list')
]