from django.contrib import admin
from .models import Project, ProjectProgress, ProjectMedia, ProjectNote


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price_per_meter', 'total_capital', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'location')


@admin.register(ProjectProgress)
class ProjectProgressAdmin(admin.ModelAdmin):
    list_display = ('project', 'date', 'predicted', 'actual')


@admin.register(ProjectMedia)
class ProjectMediaAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption', 'created_at')


@admin.register(ProjectNote)
class ProjectNoteAdmin(admin.ModelAdmin):
    list_display = ('project', 'text', 'created_at')