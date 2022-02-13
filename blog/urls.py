from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCommentView

app_name = 'blogs'

urlpatterns = [
    path('<int:pk>/comment/', BlogCommentView.as_view(), name='blog_comment'),
    path('<int:pk>/post/', BlogDetailView.as_view(), name='blog_detail'),
    path('', BlogListView.as_view(), name='blog_list')
]