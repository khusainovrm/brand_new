from django.contrib import admin
from . models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ( 'title','id', 'author', 'created_date', 'published_date')
    list_filter = ('author', 'created_date', 'published_date')
    search_fields = ('title', 'text')

class CommnentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text', 'created')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommnentAdmin)