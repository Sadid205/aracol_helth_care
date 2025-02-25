"""
URL configuration for aracol_health_care project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('category/', include('category.urls')),
    path('checkout/', include('checkout.urls')),
    path('medicine/', include('medicine.urls')),
    path('wishlist/', include('wish_list.urls')),
    path('patient/',include('patient.urls')),
    path('doctor/',include('doctor.urls')),
    path('review/',include('review.urls')),
    path('experience/',include('experience.urls')),
    path('banner/',include('banner.urls')),
    path('bmi/',include('bmi.urls')),
    path('inst_video_consult/',include('get_instance_video_consultation.urls')),
    path('consult_a_specialist/',include('consult_a_specialist.urls')),
    path('user/',include('user.urls')),
]
