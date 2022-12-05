from django.contrib import admin
from .models import SuccessAuctions, CancelledAuctions

@admin.register(SuccessAuctions)    
class SuccessAuctionsAdmin(admin.ModelAdmin):
    list_display = ['auction','bidder','bid_amount','owner'] 
    
@admin.register(CancelledAuctions)    
class CancelledAuctionsAdmin(admin.ModelAdmin):
    list_display = ['auction','cancelation_reason','cancelled_by']     
