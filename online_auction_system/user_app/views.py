from rest_framework.views import APIView
from .serializers import CountrySerializers, StateSerializers, CitySerializers, UserSerializers, BankInformation
from rest_framework import status
from rest_framework.response import Response
from .models import Country, State, City, User, BankInformation

class UserApi(APIView):
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)    