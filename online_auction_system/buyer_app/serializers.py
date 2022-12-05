from rest_framework import serializers
from .models import WishList
from user_app.serializers import UserSerializer
from auction_app.serializers import AuctionDetailsSerializer

      


class WishListSerializer(serializers.ModelSerializer):
    #user = serializers.CharField(source='user.username',read_only=True)
    #user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    #auctions = serializers.HiddenField(default = serializers.CurrentUserDefault())
    #Use= serializers.SlugRelatedField(many=True, read_only=True, slug_field='user')
    #user = UserSerializer()
    #auctions = AuctionDetailsSerializer()

    
    class Meta:
        
        model = WishList 
        fields = '__all__'
        
        
    
        
      
 
   
        