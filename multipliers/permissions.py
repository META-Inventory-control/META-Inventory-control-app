from rest_framework import permissions
from rest_framework.views import Request, View


class RecalculatePermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return False
