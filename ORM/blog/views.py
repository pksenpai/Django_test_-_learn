from django.shortcuts import render, HttpResponse
from .models import *
from django.db import connection, reset_queries
import time


"""\________________[DECORATORS]________________/"""

def run_timer(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        value = func(*args, **kwargs)
        et = time.time()
        print(f"take time = {(et - st):.3f}")
        return value
    return wrapper
      
def connection_counter(func):
    def wrapper(*args, **kwargs):
        reset_queries()
        value = func(*args, **kwargs)
        number_of_queries = len(connection.queries)
        print(f"number of connections = { number_of_queries }")
        return value
    return wrapper

"""\________________[QUERIES]________________/"""
      
@connection_counter
@run_timer
def select_related_test(request):
    test = False # ON:True | OFF:False
    
    if test:
        test_case = Blog.objects.filter(entry__headline__contains="Lennon").filter(
            entry__pub_date__year=2008
        )   
    else:
        test_case = Blog.objects.filter(entry__headline__contains="Lennon", entry__pub_date__year=2008)

    return HttpResponse(test_case)