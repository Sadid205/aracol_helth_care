from .views import CategoryModelViewset
from django.urls import path
urlpatterns = [
    path('add',CategoryModelViewset.as_view({'post':'create'}),name='category_add'),
    path('list',CategoryModelViewset.as_view({'get':'list'}),name='categories_all'),
    path('details/<int:pk>',CategoryModelViewset.as_view({'get':'retrieve'}),name='category_details'),
    path('delete/<int:pk>',CategoryModelViewset.as_view({'delete':'destroy'}),name='catetory_delete'),
    path('partial_update/<int:pk>',CategoryModelViewset.as_view({'patch':'partial_update'}),name='category_partial_update'),
    path('update/<int:pk>',CategoryModelViewset.as_view({'put':'update'}),name='category_update_all'),
]