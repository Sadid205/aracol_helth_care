from .views import MedicineModelViewSet
from django.urls import path
urlpatterns = [
    path("list",MedicineModelViewSet.as_view({"get":"list"}),name="medicine_list"),
    path("add",MedicineModelViewSet.as_view({"post":"create"}),name="medicine_add"),
    path("update/<int:pk>",MedicineModelViewSet.as_view({"put":"update"}),name="medicine_full_update"),
    path("partial_update/<int:pk>",MedicineModelViewSet.as_view({"patch":"partial_update"}),name="medicine_partial_update"),
    path("remove/<int:pk>",MedicineModelViewSet.as_view({"delete":"destroy"}),name="medicine_partial_update"),
    path("detail/<int:pk>",MedicineModelViewSet.as_view({"get":"retrieve"}),name="medicine_details"),
]