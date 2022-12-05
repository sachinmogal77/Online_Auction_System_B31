from rest_framework import viewsets, status
from .serializers import FeedBackSerializer
from .models import FeedBack
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class FeedBackViweset(viewsets.ViewSet):
    
    def create(self, request):
        serializer = FeedBackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = FeedBack.objects.all()
        serializer = FeedBackSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = FeedBack.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = FeedBackSerializer(post)
        return Response(data= serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = FeedBack.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(data={'details':'No content'}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        queryset = FeedBack.objects.all()
        post = get_object_or_404 (queryset, pk=pk)
        serializer = FeedBackSerializer(data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        queryset = FeedBack.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = FeedBackSerializer(data=request.data, instance=post, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

