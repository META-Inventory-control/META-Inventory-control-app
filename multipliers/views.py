from django.shortcuts import render
from rest_framework import generics
from .models import Multipliers
from .serializers import MultipliersSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class MultipliersView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "patch"]

    queryset = Multipliers.objects.all()
    serializer_class = MultipliersSerializer
    lookup_url_kwarg = "multipliers_id"
