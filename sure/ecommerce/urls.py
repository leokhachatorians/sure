from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('order', views.PlaceOrderView.as_view(), name='place-order'),
]
