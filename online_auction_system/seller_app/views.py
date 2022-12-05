from rest_framework.views import APIView
from .serializers import ProductInfoSerializer, ProductImageSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import ProductImages, ProductInformation


class SellerApi(APIView):
    '''
    def get(self,request):
        ProductsInfo =ProductInformation.objects.all()
        serializer = ProductInfoSerializer(ProductsInfo, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
      '''  
    def post(self,request):
        serializer = ProductInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)    


    def get(self,request,pk):
         try:
              productInfo = ProductInformation.objects.get(pk=pk)
              serializer = ProductInfoSerializer(productInfo)
              return Response(data=serializer.data,status=status.HTTP_200_OK)
         except ProductInformation.DoesNotExist:
             data = {"msg":"Record does not exist"}
             return Response(data=data,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
             productInfo = ProductInformation.objects.get(pk=pk)
             productInfo.delete()
             return Response(data={"msg":"No Content"},status=status.HTTP_204_NO_CONTENT)
        except ProductInformation.DoesNotExist:
             data = {"msg":"Record Does Not Exist"}
             return Response(data=data,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
         try:
             productInfo= ProductInformation.objects.get(pk=pk)
             serializer = ProductInfoSerializer(data=request.data,instance=productInfo,partial = True)
             if serializer.is_valid():
                 serializer.save()
                 return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
             return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
         except ProductInformation.DoesNotExist:
             data = {"msg":"Record Does Not Exist"}
             return Response(data=data,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
         try:
             productInfo= ProductInformation.objects.get(pk=pk)
             serializer = ProductInfoSerializer(data=request.data,instance=productInfo,partial = True)
             if serializer.is_valid():
                 serializer.save()
                 return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
             return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
         except ProductInformation.DoesNotExist:
             data = {"msg":"Record Does Not Exist"}
             return Response(data=data,status=status.HTTP_400_BAD_REQUEST)


       