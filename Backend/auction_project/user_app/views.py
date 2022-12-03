from rest_framework.views import APIView
from .serializers import CountrySerializer,StateSerializer,CitySerializer,UserSerializer,BankInformation
from rest_framework import status
from rest_framework.response import Response
from .models import Country,State,City,User,BankInformation


class UserApi(APIView):
    
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)






