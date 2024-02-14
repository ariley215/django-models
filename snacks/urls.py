from django.urls import path
from .views import SnackListView, SnackDetailView

urlpatterns = [
    path("", SnackListView.as_view(), name="snack_list"),
    path("snacks/", SnackListView.as_view(), name="snack_list"),
    path("snacks/<int:pk>/", SnackDetailView.as_view(), name="snack_detail"),
    path("snacks/", SnackDetailView.as_view(), name="snack_detail"),
]
