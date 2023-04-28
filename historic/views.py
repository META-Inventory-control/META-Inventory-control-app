from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Historic
from .serializers import HistoricSerializer
from products.models import Product
from django.shortcuts import get_object_or_404


# Create your views here.
class HistoricView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post"]

    queryset = Historic.objects.all()
    serializer_class = HistoricSerializer

    def perform_create(self, serializer):
        product = get_object_or_404(Product, pk=self.request._data["product"])
        product.qty = self.request._data["qty"]
        product.save()

        serializer.save()


class HistoricDetailView(generics.ListAPIView):
    serializer_class = HistoricSerializer

    def get_queryset(self):
        queryset = Historic.objects.all()
        param_value = self.kwargs.get("product_id")

        if param_value:
            queryset = queryset.filter(product_id=param_value)
        return queryset
