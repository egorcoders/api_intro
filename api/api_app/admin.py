from django.contrib import admin

from .models import Women, Category


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title',)
    search_help_text = 'Ищет бабу по названию'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

