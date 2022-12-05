from django.urls import path
from .views import AuctionDetailsViweset, CurrentAuctionsViweset, BiddersViweset,AutomaticBiddingViweset,CurrentBidsViweset,AllBidsViweset,ClosingBidViweset
urlpatterns = [
    path('auction/', AuctionDetailsViweset.as_view({'post':'create','get':'list'})),
    path('auction/<int:pk>/', AuctionDetailsViweset.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
    path('current/', CurrentAuctionsViweset.as_view({'post':'create','get':'list'})),
    path('current/<int:pk>/', CurrentAuctionsViweset.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
    path('bidders/', BiddersViweset.as_view({'post':'create','get':'list'})),
    path('bidders/<int:pk>/', BiddersViweset.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
    path('auto/', AutomaticBiddingViweset.as_view({'post':'create','get':'list'})),
    path('auto/<int:pk>/', AutomaticBiddingViweset.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
    path('currentbid/', CurrentBidsViweset.as_view({'post':'create','get':'list'})),
    path('currentbid/<int:pk>/', CurrentBidsViweset.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
    path('allbid/', AllBidsViweset.as_view({'post':'create','get':'list'})),
    path('allbid/<int:pk>/', AllBidsViweset.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
    path('closingbid/', ClosingBidViweset.as_view({'post':'create','get':'list'})),
    path('closingbid/<int:pk>/', ClosingBidViweset.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
]