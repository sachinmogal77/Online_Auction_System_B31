from rest_framework import viewsets, status
from .serializers import SuccessAuctionsSerializer, CancelledAuctionsSerializer
from .models import SuccessAuctions, CancelledAuctions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class SuccessAuctionsViweset(viewsets.ViewSet):
    
    def create(self, request):
        serializer = SuccessAuctionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = SuccessAuctions.objects.all()
        serializer = SuccessAuctionsSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = SuccessAuctions.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = SuccessAuctionsSerializer(post)
        return Response(data= serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = SuccessAuctions.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(data={'details':'No content'}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        queryset = SuccessAuctions.objects.all()
        post = get_object_or_404 (queryset, pk=pk)
        serializer = SuccessAuctionsSerializer(data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        queryset = SuccessAuctions.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = SuccessAuctionsSerializer(data=request.data, instance=post, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CancelledAuctionsViweset(viewsets.ViewSet):
    
    def create(self, request):
        serializer = CancelledAuctionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = CancelledAuctions.objects.all()
        serializer = CancelledAuctionsSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = CancelledAuctions.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = CancelledAuctionsSerializer(post)
        return Response(data= serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = CancelledAuctions.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(data={'details':'No content'}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        queryset = CancelledAuctions.objects.all()
        post = get_object_or_404 (queryset, pk=pk)
        serializer = CancelledAuctionsSerializer(data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        queryset = CancelledAuctions.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = CancelledAuctionsSerializer(data=request.data, instance=post, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
