from django.db import models


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
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Фото')
    category = models.IntegerField(verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    date_create = models.DateField(**NULLABLE, verbose_name='Дата создания', auto_now_add=True)
    date_change = models.DateField(**NULLABLE, verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.category}) - {self.price} р.'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'



