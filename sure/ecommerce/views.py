from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied, ErrorDetail
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from ecommerce.serializers import OrderSerializer, ProductSerializer, ProductDetailsSerializer
from ecommerce.models import Product


class PlaceOrderView(CreateAPIView):
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
            headers=self.headers
        )


class AvailableProductsView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
