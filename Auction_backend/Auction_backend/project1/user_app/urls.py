from django.urls import path
from .views import UserApiView, ChangePasswordView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('uv/', UserApiView.as_view(), name='userapi_url'),
    path('uv/<int:pk>/', UserApiView.as_view()),
    path('access_token/', TokenObtainPairView.as_view()),
    path('refresh_token/', TokenRefreshView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
   
]