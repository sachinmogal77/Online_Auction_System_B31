from django.contrib import admin
from .models import AuctionDetails,CurrentAuctions,CurrentBids,AllBids,AutomaticBidding,ClosingBid,Bidders

@admin.register(AuctionDetails)
class AuctionDetailAdmin(admin.ModelAdmin):
    list_display = ['product','auction_id','auction_date','auction_start_time','auction_end_time','increment_amount']

@admin.register(CurrentAuctions)
class CurrentAuctionAdmin(admin.ModelAdmin):
    list_display = ['current_auction_id','auction']

@admin.register(Bidders)
class BiddersAdmin(admin.ModelAdmin):
    list_display = ['bidder_type','bidder']

@admin.register(AutomaticBidding)
class AutomaticBiddingAdmin(admin.ModelAdmin):
    list_display = ['max_bid_amount','inc_amount','bidder','auction']

@admin.register(CurrentBids)
class CurrentBidAdmin(admin.ModelAdmin):
    list_display = ['bid_amount','bidder','auction']

class AllBidsAdmin(admin.ModelAdmin):
    list_display = ['bid_amount','bidder','auction']