from django.shortcuts import render
from django.http import HttpResponse
import time
from conf.celery import app


@app.task
def mytask():
    time.sleep(5)
    open('test.txt', 'w').close()

def home(request):

    mytask.delay()
    
    return HttpResponse('<h1>tested!!!</h1>')
