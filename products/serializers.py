from rest_framework import serializers
from .models import Product
from historic.models import Historic


class ProductSerialzier(serializers.ModelSerializer):
    final_cost = serializers.DecimalField(
        read_only=False, max_digits=7, decimal_places=2, required=False
    )
    code = serializers.CharField(read_only=True)

    def update(self, instance: Product, validated_data: dict):
        entry_cost = validated_data.pop("entry_cost", None)
        # Lógica do final price
        if entry_cost:
            setattr(instance, "entry_cost", entry_cost)
            if entry_cost <= 50:
                setattr(instance, "final_cost", entry_cost * 6)
            elif entry_cost > 50 and entry_cost <= 150:
                setattr(instance, "final_cost", entry_cost * 3)
            elif entry_cost > 151 and entry_cost <= 700:
                setattr(instance, "final_cost", entry_cost * 3)
            elif entry_cost > 701 and entry_cost <= 1500:
                calc = float(entry_cost) * 1.5
                setattr(instance, "final_cost", float(entry_cost) + calc)
            elif entry_cost > 1501 and entry_cost <= 3000:
                calc = float(entry_cost) * 0.85
                setattr(instance, "final_cost", float(entry_cost) + calc)
            elif entry_cost > 3001 and entry_cost <= 6000:
                calc = float(entry_cost) * 0.6
                setattr(instance, "final_cost", float(entry_cost) + calc)
            elif entry_cost > 6000:
                calc = float(entry_cost) * 0.45
                setattr(instance, "final_cost", float(entry_cost) + calc)

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance

    class Meta:
        model = Product
        fields = "__all__"
