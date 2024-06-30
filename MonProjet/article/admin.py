from django.contrib import admin
from . models import Articles

class AdminArticles(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'actif', 'slug', 'image']


admin.site.register(Articles, AdminArticles)
