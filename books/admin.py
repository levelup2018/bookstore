from django.contrib import admin
from .models import Book, Author, Genre

# Register your models here.

class AdminBook(admin.ModelAdmin):
    list_display = ('id', 'name', 'genre', 'user', 'price')
    list_filter = ('is_approved', 'genre', 'authors')
    prepopulated_fields = {"slug": ("name",)}
    list_editable  = ('name', 'genre', 'price')

@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Book, AdminBook)
admin.site.register(Genre)