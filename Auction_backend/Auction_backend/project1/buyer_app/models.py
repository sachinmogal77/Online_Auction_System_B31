from django.db import models
from auctions_app.models import AuctionDetails
from user_app.models import User
# Create your models here.
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    auctions = models.ForeignKey(AuctionDetails, on_delete=models.CASCADE, related_name='a_wishlist')
    