from django.urls import path
from .views import CartModelViewSet

urlpatterns = [
    path('list',CartModelViewSet.as_view({"get":"list"}),name='cart_list'),
    path('add',CartModelViewSet.as_view({"post":"create"}),name='cart_add'),
    path('remove/<int:pk>',CartModelViewSet.as_view({"delete":"destroy"}),name='cart_delete'),

]