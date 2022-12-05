from django.db import models
from auction_app.models import AuctionDetails
from user_app.models import User

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'wishlist')
    auctions = models.ForeignKey(AuctionDetails, on_delete=models.CASCADE, related_name='a_wishlist')
    
   

