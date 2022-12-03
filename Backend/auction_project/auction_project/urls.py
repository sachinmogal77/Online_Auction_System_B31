"""auction_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from auction_app.views import AuctionDetailAPI,CurrentAuctionAPI,AllAuctionApi,UpcomingAuctionApi
from seller_app.views import ProductInformationAPi
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings


router = DefaultRouter()
router.register('auction',AuctionDetailAPI,basename='auction')
router.register('cauction',CurrentAuctionAPI,basename='cauction')
router.register('allauction',AllAuctionApi,basename='allauction')
router.register('product',ProductInformationAPi,basename='product')
router.register('uauction',UpcomingAuctionApi,basename='uauction')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apiuser/',include('user_app.urls')),
    path('apiseller/',include(router.urls)),
    path('apiauction/',include(router.urls)),
    path('apiseller/access_token/',TokenObtainPairView.as_view()),
    path('apiseller/refresh_token/',TokenRefreshView.as_view()),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

