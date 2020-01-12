from rest_framework import serializers
from rest_framework.exceptions import ErrorDetail

from ecommerce.models import Customer, Order, Product, ProductDetails


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ['id']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['id']
        read_only_fields = ['name', 'image_url']


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(required=True)
    product = ProductSerializer(read_only=True)
    product_details = ProductDetailsSerializer(write_only=True)

    class Meta:
        model = Order
        fields = [
            'customer', 'product', 'product_price',
            'shipping_price', 'total_price', 'product_details',
        ]

        read_only_fields = [
            'product_price', 'shipping_price', 'total_price',
        ]

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        product_details = validated_data.pop('product_details')
        product = product_details.pop('product')
        size = product_details['size']

        if size == ProductDetails.SMALL:
            product_price = 1000
            shipping_price = 499
        elif size == ProductDetails.MEDIUM:
            product_price = 1500
            shipping_price = 599
        else:
            product_price = 2000
            shipping_price = 799

        total_price = (product_price + shipping_price)

        customer = Customer.objects.create(**customer_data)

        return Order.objects.create(
            customer=customer,
            product=product,
            size=size,
            product_price=product_price,
            shipping_price=shipping_price,
            total_price=total_price
        )
