from django.contrib import admin
from .models import Category, Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_featured", "created_at")
    list_filter = ("category", "is_featured")
    search_fields = ("title", "short_description", "description", "location")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProjectImageInline]
