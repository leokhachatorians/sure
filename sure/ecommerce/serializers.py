from rest_framework import serializers
from rest_framework.exceptions import ErrorDetail

from ecommerce.models import Customer, Order, Product, ProductDetails


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(required=True)
    product_details = ProductDetailsSerializer(write_only=True)

    class Meta:
        model = Order
        fields = [
            'customer', 'product', 'product_price',
            'shipping_price', 'total_price', 'product_details',
            'size', 'uid'
        ]

        read_only_fields = [
            'product_price', 'shipping_price', 'total_price',
            'size', 'uid'
        ]
        depth = 1

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        product_details = validated_data.pop('product_details')
        product = product_details['product']
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
