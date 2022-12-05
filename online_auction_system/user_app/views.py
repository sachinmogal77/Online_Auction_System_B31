from rest_framework import viewsets, status
from .serializers import CountrySerializer, CitySerializer, StateSerializer, UserSerializer, BankInformationSerializer
from .models import Country, State, City, User, BankInformation
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class CountryViweset(viewsets.ViewSet):
    
    def create(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = Country.objects.all()
        serializer = CountrySerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = Country.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = CountrySerializer(post)
        return Response(data= serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = Country.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(data={'details':'No content'}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        queryset = Country.objects.all()
        post = get_object_or_404 (queryset, pk=pk)
        serializer = CountrySerializer(data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        queryset = Country.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = CountrySerializer(data=request.data, instance=post, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StateViweset(viewsets.ViewSet):
    
    def create(self, request):
        serializer = StateSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = State.objects.all()
        serializer = StateSerializer (queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = State.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = StateSerializer (post)
        return Response(data= serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = State.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(data={'details':'No content'}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        queryset = State.objects.all()
        post = get_object_or_404 (queryset, pk=pk)
        serializer = StateSerializer (data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        queryset = State.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = StateSerializer (data=request.data, instance=post, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CityViweset(viewsets.ViewSet):
    
    def create(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = City.objects.all()
        serializer = CitySerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = City.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = CitySerializer(post)
        return Response(data= serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = City.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(data={'details':'No content'}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        queryset = City.objects.all()
        post = get_object_or_404 (queryset, pk=pk)
        serializer = CitySerializer(data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        queryset = City.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = CitySerializer(data=request.data, instance=post, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserViweset(viewsets.ViewSet):
    
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(post)
        return Response(data= serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = User.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(data={'details':'No content'}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        queryset = User.objects.all()
        post = get_object_or_404 (queryset, pk=pk)
        serializer = UserSerializer(data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        queryset = User.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(data=request.data, instance=post, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BankInformationViweset(viewsets.ViewSet):
    
    def create(self, request):
        serializer = BankInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = BankInformation.objects.all()
        serializer = BankInformationSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = BankInformation.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = BankInformationSerializer(post)
        return Response(data= serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = BankInformation.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(data={'details':'No content'}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        queryset = BankInformation.objects.all()
        post = get_object_or_404 (queryset, pk=pk)
        serializer = BankInformationSerializer(data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        queryset = BankInformation.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = BankInformationSerializer(data=request.data, instance=post, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
