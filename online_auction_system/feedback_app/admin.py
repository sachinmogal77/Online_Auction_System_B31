from django.contrib import admin
from .models import FeedBack

admin.site.register(FeedBack)
class feedbackAdmin(admin.ModelAdmin):
    list_display = ['email','response','feedback_date']


