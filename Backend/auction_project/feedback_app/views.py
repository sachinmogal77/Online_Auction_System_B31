from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FeedBack
from .serializers import FeedbackSerializer
from rest_framework import status
# Create your views here.

class FeedbackApi(APIView):
    def get(self,request):
        feedbacks = FeedBack.objects.all()
        serializer = FeedbackSerializer(feedbacks,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        






'''
subject = "Sending an email with Django"
            message =f'OTP {o}'
            email_from = settings.EMAIL_HOST_USER
            reciepient_list =[e]
            send_mail(subject,message,email_from,reciepient_list)
            return redirect('otp_url')

'''