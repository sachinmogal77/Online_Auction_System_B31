from rest_framework import serializers
from .models import AuctionDetails, CurrentAuctions, Bidders, AutomaticBidding, CurrentBids, AllBids, ClosingBid

class AuctionDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AuctionDetails
        fields = '__all__'
        #fields = ('auction_id',)
        
class CurrentAuctionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CurrentAuctions
        fields = '__all__'
        
class BiddersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bidders
        fields = '__all__'
        
class AutomaticBiddingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AutomaticBidding
        fields = '__all__'
        
class CurrentBidsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CurrentBids
        fields = '__all__'
        
class AllBidsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AllBids
        fields = '__all__'
        
class ClosingBidSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClosingBid
        fields = '__all__'                                                