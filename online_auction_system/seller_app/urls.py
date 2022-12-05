from django.urls import path
from .views import PorductImagesViweset, PorductInfoViweset

urlpatterns = [
    path('productinfo/', PorductInfoViweset.as_view({'post':'create','get':'list'})),
    path('productinfo/<int:pk>/', PorductInfoViweset.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
    path('productimg/', PorductImagesViweset.as_view({'post':'create','get':'list'})),
    path('productimg/<int:pk>/', PorductImagesViweset.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
]