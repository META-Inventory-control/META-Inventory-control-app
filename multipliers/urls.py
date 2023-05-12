from django.urls import path
from .views import MultipliersView
from .views import recalculate_costs

urlpatterns = [
    path(
        "multipliers/<int:multipliers_id>/",
        MultipliersView.as_view(),
        name="multipliers",
    ),
    path("multipliers/recalculate/", recalculate_costs, name="recalculate"),
]
