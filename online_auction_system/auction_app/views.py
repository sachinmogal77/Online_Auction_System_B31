from rest_framework import viewsets, status
from .serializers import AuctionDetailsSerializer, CurrentAuctionsSerializer, BiddersSerializer, AutomaticBiddingSerializer, CurrentBidsSerializer, AllBidsSerializer, ClosingBidSerializer
from .models import AuctionDetails, CurrentAuctions, Bidders, AutomaticBidding, CurrentBids, AllBids, ClosingBid
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class AuctionDetailsViweset(viewsets.ViewSet):
    
    def create(self, request):
        serializer = AuctionDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = AuctionDetails.objects.all()
        serializer = AuctionDetailsSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = AuctionDetails.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = AuctionDetailsSerializer(post)
        return Response(data= serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = AuctionDetails.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(data={'details':'No content'}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        queryset = AuctionDetails.objects.all()
        post = get_object_or_404 (queryset, pk=pk)
        serializer = AuctionDetailsSerializer(data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        queryset = AuctionDetails.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = AuctionDetailsSerializer(data=request.data, instance=post, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CurrentAuctionsViweset(viewsets.ViewSet):
    
    def create(self, request):
        serializer = CurrentAuctionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = CurrentAuctions.objects.all()
        serializer = CurrentAuctionsSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = CurrentAuctions.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = CurrentAuctionsSerializer(post)
        return Response(data= serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = CurrentAuctions.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(data={'details':'No content'}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        queryset = CurrentAuctions.objects.all()
        post = get_object_or_404 (queryset, pk=pk)
        serializer = CurrentAuctionsSerializer(data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        queryset = CurrentAuctions.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = CurrentAuctionsSerializer(data=request.data, instance=post, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BiddersViweset(viewsets.ViewSet):
    
    def create(self, request):
        serializer = BiddersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = Bidders.objects.all()
        serializer = BiddersSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = Bidders.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = BiddersSerializer(post)
        return Response(data= serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = Bidders.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(data={'details':'No content'}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        queryset = Bidders.objects.all()
        post = get_object_or_404 (queryset, pk=pk)
        serializer = BiddersSerializer(data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        queryset = Bidders.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = BiddersSerializer(data=request.data, instance=post, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class  AutomaticBiddingViweset(viewsets.ViewSet):
    
    def create(self, request):
        serializer = AutomaticBiddingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = AutomaticBidding.objects.all()
        serializer = AutomaticBiddingSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = AutomaticBidding.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = AutomaticBiddingSerializer(post)
        return Response(data= serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = AutomaticBidding.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(data={'details':'No content'}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        queryset = AutomaticBidding.objects.all()
        post = get_object_or_404 (queryset, pk=pk)
        serializer = AutomaticBiddingSerializer(data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        queryset = AutomaticBidding.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = AutomaticBiddingSerializer(data=request.data, instance=post, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CurrentBidsViweset(viewsets.ViewSet):
    
    def create(self, request):
        serializer = CurrentBidsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = CurrentBids.objects.all()
        serializer = CurrentBidsSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = CurrentBids.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = CurrentBidsSerializer(post)
        return Response(data= serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = CurrentBids.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(data={'details':'No content'}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        queryset = CurrentBids.objects.all()
        post = get_object_or_404 (queryset, pk=pk)
        serializer = CurrentBidsSerializer(data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        queryset = CurrentBids.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = CurrentBidsSerializer(data=request.data, instance=post, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AllBidsViweset(viewsets.ViewSet):
    
    def create(self, request):
        serializer = AllBidsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = AllBids.objects.all()
        serializer = AllBidsSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = AllBids.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = AllBidsSerializer(post)
        return Response(data= serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = AllBids.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(data={'details':'No content'}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        queryset = AllBids.objects.all()
        post = get_object_or_404 (queryset, pk=pk)
        serializer = AllBidsSerializer(data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        queryset = AllBids.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = AllBidsSerializer(data=request.data, instance=post, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class  ClosingBidViweset(viewsets.ViewSet):
    
    def create(self, request):
        serializer = ClosingBidSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = ClosingBid.objects.all()
        serializer = ClosingBidSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = ClosingBid.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = ClosingBidSerializer(post)
        return Response(data= serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = ClosingBid.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(data={'details':'No content'}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        queryset = ClosingBid.objects.all()
        post = get_object_or_404 (queryset, pk=pk)
        serializer = ClosingBidSerializer(data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        queryset = ClosingBid.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = ClosingBidSerializer(data=request.data, instance=post, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)                        



