from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied, ErrorDetail
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from ecommerce.serializers import OrderSerializer


class PlaceOrderView(GenericAPIView):
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(
                {'message': 'ok'},
                status=status.HTTP_200_OK,
                headers=self.headers
            )
