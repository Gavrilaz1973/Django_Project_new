from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

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

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published = True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body')
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog_list'] = Blog.objects.get(pk=self.kwargs.get('pk'))
        return context_data


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body')
    # success_url = reverse_lazy('blog')

    def get_success_url(self):
        return reverse('read_blog', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog')





