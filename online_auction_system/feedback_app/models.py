from django.db import models


class FeedBack(models.Model):
    email = models.EmailField()
    response = models.TextField()
    feedback_date = models.DateTimeField(auto_now_add = True)

    
