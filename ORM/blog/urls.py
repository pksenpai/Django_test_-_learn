from django.urls import path, include
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', test1, name='test1'),
]
