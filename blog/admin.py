from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "author", "content")
    list_filter = ("is_available", )
    search_fields = ("title", "author", "created_at")
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_available=True)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "body", "created_at")
    list_filter = ("created_at", )
    search_fields = ("post", "created_at")
 
        
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)