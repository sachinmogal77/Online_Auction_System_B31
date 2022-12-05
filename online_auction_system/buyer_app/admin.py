from django.contrib import admin
from .models import WishList



admin.site.register(WishList)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user','auctions']
