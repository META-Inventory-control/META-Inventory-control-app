from django.urls import path
from .views import MultipliersView

urlpatterns = [
    path(
        "multipliers/<int:multipliers_id>/",
        MultipliersView.as_view(),
        name="multipliers",
    )
]
