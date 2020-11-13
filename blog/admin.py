from .models import Post
from django.contrib import admin
from .models import Author, Category, Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', 'overview',)


admin.site.register(Post)
