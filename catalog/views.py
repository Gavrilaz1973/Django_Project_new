from django.shortcuts import render

from catalog.models import Product


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product(request, pk):
    context = {
        "product_list": Product.objects.get(pk=pk),
        "title": 'Информация о товаре'
    }
    return render(request, 'catalog/product.html', context)


def index(request):
    context = {
        "product_list": Product.objects.all(),
        "title": 'Информация о товаре'
    }
    return render(request, 'catalog/index.html', context)