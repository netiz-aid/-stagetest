from django.contrib import admin
from .models import Category, Tag, Task


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')
  search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')
  search_fields = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'completed', 'category', 'created_at')
  list_filter = ('completed', 'category', 'tags')
  search_fields = ('title', 'description')
  filter_horizontal = ('tags',)