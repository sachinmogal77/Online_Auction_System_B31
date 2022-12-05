from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from buyer_app.views import WishListViweset

router = DefaultRouter()
router.register('wishlist', WishListViweset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('buyer/', include(router.urls)),
    path('users/', include('user_app.urls')),
    path('seller/', include('seller_app.urls')),
    path('reports/', include('reports_app.urls')),
    path('feedback/', include('feedback_app.urls')),
    path('auctions/', include('auction_app.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
