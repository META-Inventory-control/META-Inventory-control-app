from django.shortcuts import render
from rest_framework import generics, parsers
from .models import Product
from .serializers import ProductSerialzier

# Create your views here.


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialzier

    def perform_create(self, serializer):
        # Lógica do preço final
        final_cost = int(self.request.data["entry_cost"]) * 2
        serializer.save(final_cost=final_cost)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialzier
    lookup_url_kwarg = "product_id"
