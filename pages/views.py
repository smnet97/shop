from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView
from .forms import ContactModelForm
from blog.models import BlogPostModel


class HomePageView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self, **kwargs).get_context_data()
        context['last_posts'] = BlogPostModel.objects.all().order_by('-pk')[:3]
        return context

class ContactView(CreateView):
    form_class = ContactModelForm
    template_name = 'main/contact.html'

    def get_success_url(self):
        return reverse('pages:contact')