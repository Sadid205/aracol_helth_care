from django.urls import path
from .views import CheckoutModelViewset

urlpatterns = [
    path('',CheckoutModelViewset.as_view({"post":"create"}),name="checkout_create"),
    path('list',CheckoutModelViewset.as_view({"get":"list"}),name="checkout_list"),
    path('details/<int:pk>',CheckoutModelViewset.as_view({"get":"retrieve"}),name="checkout_details"),
]