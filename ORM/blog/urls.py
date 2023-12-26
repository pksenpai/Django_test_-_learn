from django.urls import path, include
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', select_related_test, name='srt'),
]
