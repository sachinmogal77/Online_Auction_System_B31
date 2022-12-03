from django.contrib import admin
from .models import CancelledAuctions, SuccessAuctions
# Register your models here.
@admin.register(SuccessAuctions)
class SuccessAuctionsAdmin(admin.ModelAdmin):
    list_display = ('auction', 'bidder', 'bid_amount', 'owner')

@admin.register(CancelledAuctions)
class CancelledAuctionAdmin(admin.ModelAdmin):
    list_display = ('auction', 'cacelation_reason', 'cancelled_by')