from django.core.management.base import BaseCommand
from ecommerce import models

class Command(BaseCommand):
    help = 'Populate available products'

    def handle(self, *args, **kwargs):
        for _ in range(100):
            product = models.Product.objects.create()

            for size in ('s', 'm', 'l'):
                models.ProductDetails.objects.create(
                    product=product,
                    size=size
                )


