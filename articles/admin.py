from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class CommentInline(admin.TabularInline): # new
    model = Comment
    



class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = [
        "title",
        "body",
        "author",
        
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)