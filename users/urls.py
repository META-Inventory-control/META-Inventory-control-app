from django.urls import path
from .views import UserListCreateView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("users/", UserListCreateView.as_view(), name="user-list-create"),
    path("login/", TokenObtainPairView.as_view()),
    path("users/<str:user_id>/", UserDetailView.as_view()),
]
