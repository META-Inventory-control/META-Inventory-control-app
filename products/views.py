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
        # Lógica do código
        productsList = Product.objects.all()
        biggestCode = 0
        for product in productsList:
            if product.code > biggestCode:
                biggestCode = product.code

        # Lógica do preço final
        # final_cost = float(self.request.data["entry_cost"]) * 2
        entry_cost = float(self.request.data["entry_cost"])

        if entry_cost <= 50:
            final_cost = entry_cost * 6 + entry_cost
        elif entry_cost > 50 and entry_cost <= 150:
            final_cost = entry_cost * 3 + entry_cost
        elif entry_cost > 151 and entry_cost <= 700:
            final_cost = entry_cost * 2 + entry_cost
        elif entry_cost > 701 and entry_cost <= 1500:
            final_cost = entry_cost * 1.5 + entry_cost
        elif entry_cost > 1501 and entry_cost <= 3000:
            calc = entry_cost * 0.85
            final_cost = entry_cost + calc
        elif entry_cost > 3001 and entry_cost <= 6000:
            calc = entry_cost * 0.6
            final_cost = entry_cost + calc
        elif entry_cost > 6000:
            calc = entry_cost * 0.45
            final_cost = entry_cost + calc

        serializer.save(final_cost=final_cost, code=biggestCode + 1)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, ProductPermission]
    http_method_names = ["get", "patch", "delete"]

    queryset = Product.objects.all()
    serializer_class = ProductSerialzier
    lookup_url_kwarg = "product_id"
