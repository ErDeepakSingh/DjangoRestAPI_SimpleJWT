from django.core.management.base import BaseCommand,CommandError
from products.models import Product

class Command(BaseCommand):
    help = 'Fetches all the products list from database'

    def handle(self, *args, **kwargs):
        try:
            product_queryset=Product.objects.order_by('price','stock_count')
            for prod_obj in product_queryset:
                print(f"Product Name:{prod_obj.name}    |   Price:{prod_obj.price}   |   Stock Count:{prod_obj.stock_count}")
        except:
            raise CommandError('Something went wrong')



