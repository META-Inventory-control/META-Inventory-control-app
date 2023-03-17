from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .models import User


class UserDetailPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        sub_user_id = request.parser_context["kwargs"]["user_id"]
        subject_user = get_object_or_404(User, pk=sub_user_id)

        if request.user != subject_user:
            if request.user.is_superuser:
                return True
            else:
                return False
        else:
            return True
