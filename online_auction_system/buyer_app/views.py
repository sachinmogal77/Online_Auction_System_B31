from rest_framework import viewsets, status
from .serializers import WishListSerializer
from .models import WishList
from rest_framework.response import Response


class WishListViweset(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    #queryset = WishList.objects.select_related("user","auctions")

    serializer_class = WishListSerializer
    
    
    filterset_fields = ['user']
    
 

# class WishListViweset(viewsets.ViewSet):
    
#     def create(self, request):
#         serializer = WishListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def list(self, request):
#         queryset = WishList.objects.all()
#         serializer = WishListSerializer(queryset, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
    
#     def retrieve(self, request, pk=None):
#         queryset = WishList.objects.all()
#         post = get_object_or_404(queryset, pk=pk)
#         serializer = WishListSerializer(post)
#         return Response(data= serializer.data, status=status.HTTP_200_OK)
    
#     def destroy(self, request, pk=None):
#         queryset = WishList.objects.all()
#         post = get_object_or_404(queryset, pk=pk)
#         post.delete()
#         return Response(data={'details':'No content'}, status=status.HTTP_204_NO_CONTENT)
    
#     def update(self, request, pk=None):
#         queryset = WishList.objects.all()
#         post = get_object_or_404 (queryset, pk=pk)
#         serializer = WishListSerializer(data=request.data, instance=post)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def partial_update(self, request, pk=None):
#         queryset = WishList.objects.all()
#         post = get_object_or_404(queryset, pk=pk)
#         serializer = WishListSerializer(data=request.data, instance=post, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data= serializer.data, status=status.HTTP_205_RESET_CONTENT)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


