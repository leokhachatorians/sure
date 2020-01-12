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
    product_details = ProductDetailsSerializer(required=True)

    class Meta:
        model = Order
        fields = [
            'customer', 'product_details'
        ]
