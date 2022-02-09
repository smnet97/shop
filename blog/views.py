from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPostModel


class BlogListView(ListView):
    model = BlogPostModel
    template_name = 'main/blog_list.html'
    context_object_name = 'posts'


class BlogDetailView(DetailView):
    model = BlogPostModel
    template_name = 'main/blog_detail.html'
    context_object_name = 'post'
