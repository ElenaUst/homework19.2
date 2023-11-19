import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        with open('category.json', 'r', encoding='utf-8') as f:
            category_list = json.load(f)

        for category_item in category_list:
            Category.objects.create(pk=category_item['pk'], **category_item['fields'])

        with open('product.json', 'r', encoding='utf-8') as f:
            product_list = json.load(f)

        for product_item in product_list:
            product = product_item['fields']
            category_id = product.pop('category')
            Product.objects.create(pk=product_item['pk'], category_id=category_id, **product)


