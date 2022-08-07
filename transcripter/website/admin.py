from django.contrib import admin

# Register your models here.
from .models import Book


class ModelBook(admin.ModelAdmin):
    list_display = ('title','video','file_path')
    search_fields = ('author', 'title')
    list_filter = ('category', 'author')


admin.site.register(Book, ModelBook)
       