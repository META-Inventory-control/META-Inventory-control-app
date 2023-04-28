from django.shortcuts import render
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView,
)
from .serializers import UserSerializer
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import UserDetailPermission


# Create your views here.
class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["get", "post"]


class UserListView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    http_method_names = ["get"]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, UserDetailPermission]
    http_method_names = ["get", "patch", "delete"]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "user_id"
