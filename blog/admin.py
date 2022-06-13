from django.contrib import admin
from .models import Articles
# Register your models here.


class AdminArticles(admin.ModelAdmin):
    ordering = ['title', '-created']
    list_display = ['title', 'slug', 'created', 'description']

admin.site.register(Articles, AdminArticles)
