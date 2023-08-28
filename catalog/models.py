from django.db import models

from djangoProject import settings
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', **NULLABLE)
    price = models.IntegerField(verbose_name='Цена')
    date_create = models.DateField(**NULLABLE, verbose_name='Дата создания', auto_now_add=True)
    date_change = models.DateField(**NULLABLE, verbose_name='Дата изменения', auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'{self.name} ({self.category}) - {self.price} р.'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Изображение')
    date_create = models.DateField(**NULLABLE, verbose_name='Дата создания', auto_now_add=True)
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number_ver = models.CharField(max_length=50, **NULLABLE, verbose_name='Номер версии')
    name_ver = models.CharField(max_length=100, verbose_name='Название версии')
    activ_ver = models.BooleanField(default=False, verbose_name='Активная версия')

    def __str__(self):
        return self.name_ver

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'







