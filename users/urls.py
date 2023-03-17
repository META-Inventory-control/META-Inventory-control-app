from django.urls import path
from .views import UserCreateView, UserDetailView, UserListView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("users/create/", UserCreateView.as_view(), name="user-create"),
    path("users/list/", UserListView.as_view(), name="user-list"),
    path("login/", TokenObtainPairView.as_view(), name="user-login"),
    path("users/<str:user_id>/", UserDetailView.as_view(), name="user-detail"),
]
