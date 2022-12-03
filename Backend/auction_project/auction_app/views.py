from django.shortcuts import render
from rest_framework.views import APIView
from .models import AuctionDetails,CurrentAuctions
from .serializers import AuctionDetailSerializer,CurrentAuctionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.utils import timezone
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from datetime import date,datetime,timedelta


# class AuctionDetailAPI(viewsets.ModelViewSet):
#     queryset = AuctionDetails.objects.all()
#     serializer_class = AuctionDetailSerializer
#     http_method_names = ['post','get']


class AuctionDetailAPI(viewsets.ViewSet):
    def create(self,request):
        serializer = AuctionDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def list(self,request):
        userdate = datetime.today() - timedelta(days=2)
        print(userdate)
        previous_date = datetime.today()-timedelta(days=1)
        upcoming_date = datetime.today()+ timedelta(days=1)
        
        if userdate < previous_date:

            queryset = AuctionDetails.objects.filter(auction_date__lte=previous_date,auction_date__month='11',auction_date__year='2022')

            serializer = AuctionDetailSerializer(queryset,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            queryset = AuctionDetails.objects.filter(product=5,auction_date__gte=upcoming_date,auction_date__month='11',auction_date__year='2022')
            serializer = AuctionDetailSerializer(queryset,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)

class AllAuctionApi(viewsets.ModelViewSet):
        #queryset = AuctionDetails.objects.select_related('product').all()
        #queryset=AuctionDetails.objects.all().prefetch_related('product')
       
        queryset = AuctionDetails.objects.all()
        print(queryset)    
        serializer_class = AuctionDetailSerializer
        http_method_names = ['get']

class UpcomingAuctionApi(viewsets.ModelViewSet):
        upcoming_date = datetime.today()+timedelta(days=1)

        queryset = AuctionDetails.objects.filter(auction_date__gte=upcoming_date)
        serializer_class = AuctionDetailSerializer
        http_method_names = ['get']


class CurrentAuctionAPI(viewsets.ModelViewSet):
   start_date = datetime.today()
   end_date = start_date+timedelta(days=1)

   queryset = AuctionDetails.objects.filter(auction_date__range=[start_date,end_date])
   serializer_class = AuctionDetailSerializer
   http_method_name = ['get']

    

'''
class AuctionDetailApi(APIView):
    def get(self,request):
         auctionDetail=AuctionDetails.objects.all()
         serializer = AuctionDetailSerializer(auctionDetail,many=True)
         return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = AuctionDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AuctionDetailDetailApi(APIView):
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
'''            





        

