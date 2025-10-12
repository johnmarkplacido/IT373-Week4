from django.contrib import admin
from pages.models import Post, Comment, Student, Course, Enrollment
from .models import Author, Category, Book
# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1

admin.site.register(Author)
admin.site.register(Book)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "created_at")
    search_fields = ("title", "body")
    list_filter = ("created_at",)
    ordering = ("-created_at",)