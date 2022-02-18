from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class ShopView(ListView):
    model = ProductModel
    paginate_by = 3
    template_name = 'main/shop.html'


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'main/product_detail.html'
