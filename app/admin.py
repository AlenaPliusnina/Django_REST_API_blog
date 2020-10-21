from django.contrib import admin
from app.models import Post, Category


@admin.register(Post)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'content', 'updated', 'publication_date')


@admin.register(Category)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name')