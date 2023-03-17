from rest_framework import serializers
from .models import Product


class ProductSerialzier(serializers.ModelSerializer):
    final_cost = serializers.DecimalField(
        read_only=True, max_digits=7, decimal_places=2
    )

    def update(self, instance: Product, validated_data: dict):
        entry_cost = validated_data.pop("entry_cost", None)
        # Lógica do final price
        if entry_cost:
            setattr(instance, "entry_cost", entry_cost)
            setattr(instance, "final_cost", entry_cost * 2)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = Product
        fields = "__all__"
