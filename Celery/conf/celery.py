from celery import Celery
import os


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

app = Celery('ccore')
app.config_from_object(
    'django.conf:settings', 
    namespace='CELERY',
)
