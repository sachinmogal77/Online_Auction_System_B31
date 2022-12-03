from django.contrib import admin
from .models import AuctionDetails, CurrentAuctions, Bidders, AutomaticBidding, CurrentBids, AllBids, ClosingBid

# Register your models here.
@admin.register(AuctionDetails)
class AuctionDetailsAdmin(admin.ModelAdmin):
    list_display = ('product','auction_id', 'auction_date','auction_start_time','auction_end_time', 'increment_amount')

@admin.register(CurrentAuctions)
class CurrentAuctionAdmin(admin.ModelAdmin):
    list_display = ('current_auction_id', 'auction')

@admin.register(Bidders)
class BiddersAdmin(admin.ModelAdmin):
    list_display = ('bidder_type', 'bidder')



