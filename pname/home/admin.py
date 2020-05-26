from django.contrib import admin

# Register your models here.
from .models import Post,Comment
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish',   
                       'status')
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('post', 'name', 'email', 'body')
# from django.contrib import admin
# from .models import Post, Comment


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'author', 'publish',   
#                        'status')
    


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin): 
#     list_display = ('post', 'name', 'email', 'body')
    