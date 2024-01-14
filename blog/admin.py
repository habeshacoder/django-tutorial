from django.contrib import admin
from blog.models import Post, Author, Tag
class PostAdmin(admin.ModelAdmin):
    list_display=('title','date','author')
    prepopulated_fields={"slug":('title',)}
class AuthorAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email')
# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag)