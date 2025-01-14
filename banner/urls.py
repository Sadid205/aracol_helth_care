
from .views import BannerModelView
from django.urls import path
urlpatterns = [
    path('add',BannerModelView.as_view({"post":"create"}),name='banner'),
    path('list/',BannerModelView.as_view({"get":"list"}),name='banner_list'),
    path('update/<int:pk>/',BannerModelView.as_view({"put":"update"}),name='banner_update'),
    path('delete/<int:pk>/',BannerModelView.as_view({"delete":"destroy"}),name='banner_delete'),
]