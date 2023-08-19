from django.contrib import admin
from .models import Category, BlogPost, Reaction, Comment


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "author", "date_published"]
