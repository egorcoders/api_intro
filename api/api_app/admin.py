from django.contrib import admin

from .models import MarriedWomen, Category, DivorcedWomen


@admin.register(MarriedWomen)
class MarriedWomen(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title',)
    search_help_text = 'Ищет бабу по названию'


@admin.register(DivorcedWomen)
class DivorcedWomen(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title',)
    search_help_text = 'Ищет бабу по названию'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

