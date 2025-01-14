
from .views import UserLoginAPIView,UserLogoutAPIView
from django.urls import path
urlpatterns = [
    path('login',UserLoginAPIView.as_view(),name="login"),    
    path('logout',UserLogoutAPIView.as_view(),name="logout")    
]