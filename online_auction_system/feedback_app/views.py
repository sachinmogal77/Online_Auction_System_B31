
from .serializers import FeedBackSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import FeedBack
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
from .serializers import FeedBackSerializer


class FeedbackAPI(APIView):
    
    def get(self, request):
        feedback = FeedBack.objects.all()
        serializer = FeedBackSerializer(feedback, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def post(self,request):
        serializer = FeedBackSerializer(data=request.data)
        email = request.POST['email']
        user = FeedBack.objects.create(
            email = email
            
        )
        if serializer.is_valid():
            subject = 'Online Auction System'
            message = 'Thank You For Your Feedback.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email,]
            send_mail( subject, message, email_from, recipient_list )
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)        

    








       


    

   


    

    






    #def get(self, request):
     #   feedback = FeedBack.objects.all()
      #  serializer = FeedBackSerializer(feedback, many=True)
       # return Response(data=serializer.data, status=status.HTTP_200_OK)


    #def post(self,request):
     #   serializer = FeedBackSerializer(data=request.data)
      #  if serializer.is_valid():
       #     serializer.save()
        #    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        #return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)        