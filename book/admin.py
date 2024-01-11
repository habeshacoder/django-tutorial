from django.contrib import admin
from .models import Book, Author, Address

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ('title', 'author') 
    list_filter = ('title', 'author')  
    search_fields = ('title', 'author')
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
# Register your models here.
