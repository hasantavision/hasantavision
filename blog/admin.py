from django.contrib import admin
from .models import Post
from comments.models import Comment


# Register your models here.
class CommentInLine(admin.TabularInline):
    model = Comment


class BlogAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]
    list_display = ("title", "author", "date")


admin.site.register(Post, BlogAdmin)
