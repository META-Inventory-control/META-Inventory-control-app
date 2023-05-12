from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Group
from .serializers import GroupSerialzier

# Create your views here.


class GroupView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post"]

    queryset = Group.objects.all()
    serializer_class = GroupSerialzier


class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    http_method_names = ["get", "patch", "delete"]

    queryset = Group.objects.all()
    serializer_class = GroupSerialzier
    lookup_url_kwarg = "group_id"
