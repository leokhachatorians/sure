import uuid

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=32)
    image_url = models.CharField(max_length=255, default='http://lorempixel.com/output/animals-q-c-640-480-4.jpg')

    def __str__(self):
        return self.name


class ProductDetails(models.Model):
    SMALL = 's'
    MEDIUM = 'm'
    LARGE = 'l'

    SIZE_CHOICES = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large')
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    size = models.CharField(max_length=6, choices=SIZE_CHOICES, default=SMALL)


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=13)
    address_1 = models.TextField()
    address_2 = models.TextField()
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=12)
    country = models.CharField(max_length=255)


class Order(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    product = models.ForeignKey(Product, related_name='order_product', on_delete=models.DO_NOTHING)
    product_details = models.ForeignKey(Product, related_name='order_product_details', on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, related_name='customer')
    product_price = models.IntegerField(default=1000)
    shipping_price = models.IntegerField(default=499)
    total_price = models.IntegerField(default=1499)
