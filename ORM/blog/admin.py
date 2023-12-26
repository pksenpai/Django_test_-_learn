from django.contrib import admin
from .models import *


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin): ...

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin): ...

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin): ...
