from django.urls import path
from . views import UserApi

urlpatterns = [
    path('user/',UserApi.as_view())
]