from django.urls import path
from .views import SuccessAuctionsViweset, CancelledAuctionsViweset

urlpatterns = [
    path('success/', SuccessAuctionsViweset.as_view({'post':'create','get':'list'})),
    path('success/<int:pk>/', SuccessAuctionsViweset.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
    path('cancelled/', CancelledAuctionsViweset.as_view({'post':'create','get':'list'})),
    path('cancelled/<int:pk>/', CancelledAuctionsViweset.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
]