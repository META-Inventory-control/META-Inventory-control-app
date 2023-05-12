from rest_framework import serializers
from .models import Product
from historic.models import Historic
from django.shortcuts import get_object_or_404
from multipliers.models import Multipliers


class ProductSerialzier(serializers.ModelSerializer):
    final_cost = serializers.DecimalField(
        read_only=False, max_digits=7, decimal_places=2, required=False
    )
    code = serializers.CharField(read_only=True)

    def update(self, instance: Product, validated_data: dict):
        entry_cost = validated_data.pop("entry_cost", None)
        final_cost_pop = validated_data.pop("final_cost", None)
        multipliers = get_object_or_404(Multipliers, pk=1)
        # Lógica do final price
        if entry_cost:
            setattr(instance, "entry_cost", entry_cost)
            if entry_cost <= 50:
                setattr(
                    instance,
                    "final_cost",
                    entry_cost * multipliers.multi_0_50 / 100 + entry_cost,
                )
            elif entry_cost > 50 and entry_cost <= 150:
                setattr(
                    instance,
                    "final_cost",
                    entry_cost * multipliers.multi_51_150 / 100 + entry_cost,
                )
            elif entry_cost > 151 and entry_cost <= 700:
                setattr(
                    instance,
                    "final_cost",
                    entry_cost * multipliers.multi_151_700 / 100 + entry_cost,
                )
            elif entry_cost > 701 and entry_cost <= 1500:
                setattr(
                    instance,
                    "final_cost",
                    entry_cost * multipliers.multi_701_1500 / 100 + entry_cost,
                )
            elif entry_cost > 1501 and entry_cost <= 3000:
                setattr(
                    instance,
                    "final_cost",
                    entry_cost * multipliers.multi_1501_3000 / 100 + entry_cost,
                )
            elif entry_cost > 3001 and entry_cost <= 6000:
                setattr(
                    instance,
                    "final_cost",
                    entry_cost * multipliers.multi_3001_6000 / 100 + entry_cost,
                )
            elif entry_cost > 6000:
                setattr(
                    instance,
                    "final_cost",
                    entry_cost * multipliers.multi_6001_8 / 100 + entry_cost,
                )

        if entry_cost and not final_cost_pop:
            setattr(instance, "final_cost_altered", False)

        if final_cost_pop:
            setattr(instance, "final_cost_altered", True)
            setattr(instance, "final_cost", final_cost_pop)

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance

    class Meta:
        model = Product
        fields = "__all__"
