from django.contrib import admin
from .models import AuctionDetails, CurrentAuctions,ClosingBid, CurrentBids,AutomaticBidding,AllBids, Bidders

admin.site.register(AuctionDetails)
class AuctionDetailAdmin(admin.ModelAdmin):
    list_display = ['product','auction_id','auction_date','auction_start_time','auction_end_time','increment_amount']


admin.site.register(CurrentAuctions)
class CurrentAuctionAdmin(admin.ModelAdmin):
    list_display = ['current_auction_id','auction'] 

admin.site.register(ClosingBid)
class ClosingBidAdmin(admin.ModelAdmin):
    list_display = ['closing_bid_amount','bidder','auction']      


admin.site.register(CurrentBids)
class CurrentBidsAdmin(admin.ModelAdmin):
    list_display = ['bid_amount','bidder','auction']


admin.site.register(AutomaticBidding)
class AutomaticBiddingAdmin(admin.ModelAdmin):
    list_display = ['max_bid_amount','inc_amount','bidder','auction']


admin.site.register(AllBids)
class AllBidsAdmin(admin.ModelAdmin):
    list_display = ['bid_amount','bidder','auction']  

admin.site.register(Bidders)
class BiddersAdmin(admin.ModelAdmin):
    list_display = ['bidder_type','bidder']     