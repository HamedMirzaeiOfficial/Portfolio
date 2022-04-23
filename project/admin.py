from django.contrib import admin
from .models import Project, CategoryProject


@admin.register(CategoryProject)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'last_modified')
    list_filter = ('created_on', 'last_modified')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'body',  'created_on',
                    'last_modified', 'active')
    list_filter = ('created_on', 'last_modified', 'active')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'created_on'
    ordering = ('active', 'created_on')
