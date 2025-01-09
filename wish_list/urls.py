from django.urls import path
from .views import WishListModelViewset

urlpatterns = [
    path('list',WishListModelViewset.as_view({"get":"list"}),name="wish_list_list"),
    path('add',WishListModelViewset.as_view({"post":"create"}),name="wish_list_add"),
    path('remove/<int:pk>',WishListModelViewset.as_view({"delete":"destroy"}),name="wish_list_delete"),
]