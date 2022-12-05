from django.contrib import admin

from .models import AuctionDetails, AllBids ,AutomaticBidding, CurrentAuctions, Bidders, CurrentBids, ClosingBid

@admin.register(AuctionDetails)    
class AuctionDetailsAdmin(admin.ModelAdmin):
    list_display = ['product','auction_date','auction_start_time','auction_end_time','increment_amount'] 

@admin.register(AllBids)    
class AllBidsAdmin(admin.ModelAdmin):
    list_display = ['bid_amount','bidder','auction'] 
    
@admin.register(AutomaticBidding)    
class AutomaticBiddingAdmin(admin.ModelAdmin):
    list_display = ['max_bid_amount','inc_amount','bidder','auction'] 
    
@admin.register(CurrentAuctions)    
class CurrentAuctionsAdmin(admin.ModelAdmin):
    list_display = ['current_auction_id','auction'] 
    
@admin.register(Bidders)    
class BiddersAdmin(admin.ModelAdmin):
    list_display = ['bidder_type','bidder'] 
    
@admin.register(CurrentBids)    
class CurrentBidsAdmin(admin.ModelAdmin):
    list_display = ['bid_amount','bidder','auction'] 
    
@admin.register(ClosingBid)    
class ClosingBidAdmin(admin.ModelAdmin):
    list_display = ['closing_bid_amount','bidder','auction']                     