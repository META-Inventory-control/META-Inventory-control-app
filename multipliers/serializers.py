from rest_framework import serializers
from .models import Multipliers


class MultipliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multipliers
        fields = "__all__"
