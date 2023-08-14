from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'name': 'aser', 'description': '2-х ядерный', 'category': '2', 'price': '40000'},
            {'name': 'hp', 'description': '4-х ядерный', 'category': '2', 'price': '60000'},
        ]
        category_list = [
            {'name': 'компьютер', 'description': 'стационарный компьютер'}
        ]

        Product.objects.all().delete()
        Category.objects.all().delete()

        for category_item in category_list:
            Category.objects.create(**category_item)

        for product_item in product_list:
            Product.objects.create(**product_item)