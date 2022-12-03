import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auction_project.settings")
app = Celery("auction_project")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()