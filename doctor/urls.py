from django.urls import path
from .views import DoctorModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'doctors',DoctorModelViewSet,basename='doctor')
urlpatterns = [
    path('update/<int:pk>/',DoctorModelViewSet.as_view({"put":"update"}),name="doctor_update"),
    path('list/',DoctorModelViewSet.as_view({"get":"list"}),name="doctor_list")
]

urlpatterns+=router.urls