from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from catalog.models import Product, Blog


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты'
    }


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data['product_list'] = Product.objects.get(pk=self.kwargs.get('pk'))
        return context_data


class IndexListView(ListView):
    template_name = 'catalog/index.html'
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.all()
        return queryset


class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body')
    success_url = reverse_lazy('index')


class BlogDetailView(DetailView):
    model = Blog

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog_list'] = Blog.objects.get(pk=self.kwargs.get('pk'))
        return context_data





