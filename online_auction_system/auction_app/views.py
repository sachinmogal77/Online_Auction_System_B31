from rest_framework.views import APIView
from .serializers import AuctionDetailSerializer, CurrentAuctionSerializer, AutomaticBidSerializer,BidderSerializer,AllBiddSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import AuctionDetails,AutomaticBidding,CurrentAuctions


class AuctionDetailApi(APIView):
    '''
    def get(self,request):
        AuctionInfo =AuctionDetails.objects.all()
        serializer = AuctionDetailSerializer(AuctionInfo, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
      '''  
    def post(self,request):
        serializer = AuctionDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)    



    def get(self,request,pk):
        try:
            auctionDetail = AuctionDetails.objects.get(pk=pk)
            serializer = AuctionDetailSerializer(auctionDetail)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except AuctionDetails.DoesNotExist:
            data = {"msg":"Record Does not exist"}
        return Response(data=data,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        try:
            auctionDetail = AuctionDetails.objects.get(pk=pk)
            auctionDetail.delete()
            return Response(data={"msg":"No Content"},status=status.HTTP_204_NO_CONTENT)
        except AuctionDetails.DoesNotExist:
            data = {"msg":"Record Does Not Exist"}
            return Response(data=data,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        try:
            auctionDetail = AuctionDetails.objects.get(pk=pk)
            serializer= AuctionDetailSerializer(data=request.data,instance=auctionDetail,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except AuctionDetails.DoesNotExist:
            data = {"msg":"Record Does Not exist"}
            return Response(data=data,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        try:
            auctionDetail = AuctionDetails.objects.get(pk=pk)
            serializer = AuctionDetailSerializer(data=request.data,instance=auctionDetail,partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except AuctionDetails.DoesNotExist:
            data = {"msg":"Record Does Not Exist"}
            return Response(data=data,status=status.HTTP_400_BAD_REQUEST)
