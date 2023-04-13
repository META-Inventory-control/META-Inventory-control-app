from django.shortcuts import render
from rest_framework import generics, parsers
from .models import Product
from .serializers import ProductSerialzier
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import ProductPermission
from groups.models import Group

# Create your views here.


class ProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, ProductPermission]
    http_method_names = ["get", "post"]

    queryset = Product.objects.all()
    serializer_class = ProductSerialzier

    def perform_create(self, serializer):
        # Lógica do preço final
        final_cost = float(self.request.data["entry_cost"]) * 2
        serializer.save(final_cost=final_cost)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, ProductPermission]
    http_method_names = ["get", "patch", "delete"]

    queryset = Product.objects.all()
    serializer_class = ProductSerialzier
    lookup_url_kwarg = "product_id"
