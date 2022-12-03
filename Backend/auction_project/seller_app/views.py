from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductInformationSerializer,ProductImagesSerializer
from .models import ProductInformation,ProductImages
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class ProductInformationAPi(viewsets.ModelViewSet):
    queryset = ProductInformation.objects.all()
    serializer_class = ProductInformationSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

# class SellerApi(APIView):
#     def get(self,request):
#         productsInfo =ProductInformation.objects.all()
#         serializer = ProductInformationSerializer(productsInfo,many=True)
#         return Response(data=serializer.data,status=status.HTTP_200_OK)
         
#     def post(self,request):
#         serializer = ProductInformationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data,status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class SellerDetailApi(APIView):
#     def get(self,request,pk):
#         try:
#              productInfo = ProductInformation.objects.get(pk=pk)
#              serializer = ProductInformationSerializer(productInfo)
#              return Response(data=serializer.data,status=status.HTTP_200_OK)
#         except ProductInformation.DoesNotExist:
#             data = {"msg":"Record does not exist"}
#             return Response(data=data,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,pk):
#         try:
#             productInfo = ProductInformation.objects.get(pk=pk)
#             productInfo.delete()
#             return Response(data={"msg":"No Content"},status=status.HTTP_204_NO_CONTENT)
#         except ProductInformation.DoesNotExist:
#             data = {"msg":"Record Does Not Exist"}
#             return Response(data=data,status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self,request,pk):
#         try:
#             productInfo= ProductInformation.objects.get(pk=pk)
#             serializer = ProductInformationSerializer(data=request.data,instance=productInfo,partial = True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
#             return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#         except ProductInformation.DoesNotExist:
#             data = {"msg":"Record Does Not Exist"}
#             return Response(data=data,status=status.HTTP_400_BAD_REQUEST)

#     def patch(self,request,pk):
#         try:
#             productInfo= ProductInformation.objects.get(pk=pk)
#             serializer = ProductInformationSerializer(data=request.data,instance=productInfo,partial = True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
#             return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#         except ProductInformation.DoesNotExist:
#             data = {"msg":"Record Does Not Exist"}
#             return Response(data=data,status=status.HTTP_400_BAD_REQUEST)





