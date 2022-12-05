from rest_framework import serializers
from .models import AuctionDetails, CurrentAuctions,ClosingBid, CurrentBids,AutomaticBidding,AllBids, Bidders


class AuctionDetailSerializer(serializers.ModelSerializer):
    class Meta:

        model = AuctionDetails
        fields = '__all__'

class CurrentAuctionSerializer(serializers.ModelSerializer):
    class Meta:

        model = CurrentAuctions
        fields = '__all__'

class BidderSerializer(serializers.ModelSerializer):
    class Meta:

        model = Bidders
        fields = '__all__'

class ClosingBidSerializer(serializers.ModelSerializer):
    class Meta:

        model = ClosingBid
        fields = '__all__'            


class CurrentBidSerializer(serializers.ModelSerializer):
    class Meta:

        model = CurrentBids
        fields = '__all__'        


class AutomaticBidSerializer(serializers.ModelSerializer):
    class Meta:

        model = AutomaticBidding
        fields = '__all__'  

class AllBiddSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllBids
        fields = '__all__'              