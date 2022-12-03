
from rest_framework.reverse import reverse
from .models import User
from.serializers import UserSerializer, ChangePasswordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class UserApiView(APIView):
    permission_classes = [IsAuthenticated,IsAdminUser, IsOwnerOrReadOnly]
    def get(self,request):
        userobj= User.objects.all()
        serializer = UserSerializer(userobj, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data= serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

    def put(self,request,pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(data= request.data, instance=user, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(data= serializer.data, status= status.HTTP_205_RESET_CONTENT)
            return Response(data= serializer.errors, status= status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            data = {'msg': 'User Does Not Exist'}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(data= {'msg': 'No Content'}, status= status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            data = {'msg': 'User Does Not Exist'}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

