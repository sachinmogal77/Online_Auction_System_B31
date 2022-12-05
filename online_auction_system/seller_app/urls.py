from django.urls import path
from .views import SellerApi

urlpatterns = [
    path('seller/',SellerApi.as_view())
]