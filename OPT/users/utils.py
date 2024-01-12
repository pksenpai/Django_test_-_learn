from django.core.cache import cache
from django.utils.crypto import get_random_string
from django.shortcuts import render


def store_otp(key):

    value = cache.get(key)
    if value is None:
        value = get_random_string(7)
        cache.set(key, value, timeout=120)
        
    return value

