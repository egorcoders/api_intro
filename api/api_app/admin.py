from django.contrib import admin

from .models import Women, Category
from api.settings import DEFAULT_NUMBER


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


admin.site.register(Category)
