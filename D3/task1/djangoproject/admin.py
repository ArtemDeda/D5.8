from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_published')
    readonly_fields = ('date_published',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(News, NewsAdmin)