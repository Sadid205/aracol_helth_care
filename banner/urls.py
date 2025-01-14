
from .views import BannerModelView
from django.urls import path
urlpatterns = [
    path('add',BannerModelView.as_view({"post":"create"}),name='add_banner'),
    path('list/',BannerModelView.as_view({"get":"list"}),name='banner_list'),
]