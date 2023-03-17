from rest_framework import serializers
from .models import Product


class ProductSerialzier(serializers.ModelSerializer):
    final_cost = serializers.DecimalField(
        read_only=True, max_digits=7, decimal_places=2
    )

    class Meta:
        model = Product
        fields = "__all__"
