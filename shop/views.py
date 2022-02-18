from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class ShopView(ListView):
    model = ProductModel
    paginate_by = 3
    template_name = 'main/shop.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ShopView, self, *args, **kwargs).get_context_data()
        context['categories'] = CategoryModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['tags'] = TagModel.objects.all()
        return context

    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(name__icontains=q)
            return qs

        cat = self.request.GET.get('cat')
        if cat:
            qs = qs.filter(category_id=cat)
            return qs

        brand = self.request.GET.get('brand')
        if brand:
            qs = qs.filter(brand_id=brand)

        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tag__name=tag)
            return qs
        return qs


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'main/product_detail.html'
