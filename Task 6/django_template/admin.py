from django.contrib import admin
from .models import bookStore
# Register your models here.


class BookStoreDB(admin.ModelAdmin):
    list_display=[ 'book_title','book_author','year_published']



admin.site.register(bookStore,BookStoreDB)