from django.db.models import Min, Max
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
        context['sizes'] = SizeModel.objects.all()
        context['colors'] = ColorModel.objects.all()

        # select avg(salary) as sum_salary from emp

        # context['min_price'], context['max_price']

        context['min_price'], context['max_price'] = ProductModel.objects.aggregate(
            Min('real_price'),
            Max('real_price')
        ).values()



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


        brand = self.request.GET.get('brand')
        if brand:
            qs = qs.filter(brand_id=brand)

        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tag__id=tag)

        size = self.request.GET.get('size')
        if size:
            qs = qs.filter(size__id=size)

        color = self.request.GET.get('color')
        if color:
            qs = qs.filter(color__id=color)

        price_sort = self.request.GET.get('price_sort')
        if price_sort == 'price':
            qs = qs.order_by('real_price')
        elif price_sort == '-price':
            qs = qs.order_by('-real_price')

        price = self.request.GET.get('price')
        if price:
            min, max = price.split(';')
            qs = qs.filter(real_price__gte=min, real_price__lte=max)

        return qs


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'main/product_detail.html'
