from rest_framework import serializers
from .models import Historic


class HistoricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historic
        fields = "__all__"
