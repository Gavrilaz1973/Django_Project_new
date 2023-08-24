from django.contrib import admin

from catalog.models import Category, Product, Blog, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ("category",)
    search_fields = ('name', 'description',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'is_published', 'views_count',)
    list_filter = ("is_published",)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'number_ver',)
    list_filter = ('activ_ver',)


