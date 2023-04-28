from django.urls import path
from .views import HistoricView, HistoricDetailView

urlpatterns = [
    path("historic/", HistoricView.as_view(), name="historic-list-create"),
    path(
        "historic/<str:product_id>/",
        HistoricDetailView.as_view(),
        name="historic-retrieve",
    ),
]
