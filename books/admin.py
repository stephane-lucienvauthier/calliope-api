"""This module manages the admin section for the products app."""
from django.contrib import admin
from .models import Book, Tag

admin.site.register(Book)
admin.site.register(Tag)
