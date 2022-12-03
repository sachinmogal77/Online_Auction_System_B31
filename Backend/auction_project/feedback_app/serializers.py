#from time import sleep
from rest_framework import serializers
#from django.core.mail import send_mail
from . import models
from feedback_app.tasks import send_feedback_email_task


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FeedBack
        fields = '__all__'

    
    def send_email(self):
        send_feedback_email_task.delay(
            self.cleaned_data["email"], self.cleaned_data["response"]
        )