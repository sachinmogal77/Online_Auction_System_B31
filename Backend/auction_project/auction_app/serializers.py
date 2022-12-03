from rest_framework import serializers
from .models import AuctionDetails,CurrentAuctions,Bidders,AllBids,ClosingBid,CurrentBids,AutomaticBidding
from user_app.models import User
import datetime
from datetime import timedelta
import _strptime
from seller_app.serializers import ProductInformationSerializer

class AuctionDetailSerializer(serializers.ModelSerializer):
    #product = AuctionDetails.objects.select_related('product').all()
    #product = ProductInformationSerializer(read_only=True)
    auction_date = serializers.DateField()
    auction_start_time = serializers.TimeField()
    auction_end_time = serializers.TimeField()
    today = datetime.datetime.today()
    
    class Meta:
        model = AuctionDetails
        fields = ['product','auction_id','auction_date','auction_start_time','auction_end_time','increment_amount']
        
        
        obj = AuctionDetails.objects.get(product=5)
        print(obj)

    def validate(self, attrs):
        auction_date = attrs.get('auction_date')
        print('-------------------------------------------------------------------')
        today = datetime.date.today()
        #+timedelta(days=1)
        print(type(today))
        print(type('auction_date'))
        #date = datetime.strptime('auction_date', '%Y-%m-%d %H:%M:%S')
        if auction_date < today :
            print(type(auction_date))
            raise serializers.ValidationError("Previous Date not allowed and add auction for next two days from today")
        return attrs


    # def save(self):
    #     auction = AuctionDetails
    #     auction_date = self.validated_data['auction_date']
    #     date = datetime.date.today()+ timedelta(days=2)
    #     #+timedelta(days=2)

    #     if auction_date <= date:
    #         raise serializers.ValidationError('plz add auction for next two days')
    #     return auction


    # def validate(self, attrs):
    #     if attrs['auction_date'] >= datetime.():
    #         raise serializers.ValidationError(
    #             "Previous Date is not allowed"
    #         )
    #     return attrs

    #def validate(self, data):
        # if data['auction_date'] >= datetime.today():
        #     print(datetime.today)
        #     raise serializers.ValidationError(
        #         "Date must be today or within 7 days")
        # print(data)
        # return data
        
        #print(datetime.today)
   # def validate(self, attrs):
        #today = datetime.date.today()
        #current_time = datetime.date.now()
        #s = current_time.time
        #rint(s)
        #print(today)


class CurrentAuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentAuctions
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)

    

class BiddersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bidders
        fields = '__all__'

class AllBidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllBids
        fields = '__all__'

class ClosingBidSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClosingBid
        fields = '__all__'

class CurrentBidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentBids
        fields = '__all__'

class AutomaticBidding(serializers.ModelSerializer):
    class Meta:
        model = AutomaticBidding
        fields = '__all__'

