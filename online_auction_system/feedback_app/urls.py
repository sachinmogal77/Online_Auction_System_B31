from django.urls import path
from .views import FeedBackViweset

urlpatterns = [
    path('feedback/', FeedBackViweset.as_view({'post':'create','get':'list'})),
    path('feedback/<int:pk>/', FeedBackViweset.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
    
]