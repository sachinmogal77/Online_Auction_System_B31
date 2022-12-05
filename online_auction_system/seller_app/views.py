from rest_framework import viewsets, status
from .serializers import ProductImagesSerializer, ProductInformationSerializer
from .models import ProductInformation, ProductImages
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class PorductInfoViweset(viewsets.ViewSet):
    
    def create(self, request):
        serializer = ProductInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = ProductInformation.objects.all()
        serializer = ProductInformationSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = ProductInformation.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = ProductInformationSerializer(post)
        return Response(data= serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = ProductInformation.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(data={'details':'No content'}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        queryset = ProductInformation.objects.all()
        post = get_object_or_404 (queryset, pk=pk)
        serializer = ProductInformationSerializer(data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        queryset = ProductInformation.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = ProductInformationSerializer(data=request.data, instance=post, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PorductImagesViweset(viewsets.ViewSet):
    
    def create(self, request):
        serializer = ProductImagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = ProductImages.objects.all()
        serializer = ProductImagesSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = ProductImages.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = ProductImagesSerializer(post)
        return Response(data= serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = ProductImages.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(data={'details':'No content'}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        queryset = ProductImages.objects.all()
        post = get_object_or_404 (queryset, pk=pk)
        serializer = ProductImagesSerializer(data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        queryset = ProductImages.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = ProductImagesSerializer(data=request.data, instance=post, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


