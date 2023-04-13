from django.urls import path
from .views import GroupView, GroupDetailView

urlpatterns = [
    path("groups/", GroupView.as_view(), name="group-list-create"),
    path("groups/<str:group_id>/", GroupDetailView.as_view(), name="group-detail-view"),
]
