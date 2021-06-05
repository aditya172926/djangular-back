from django.contrib import admin
from .models import Movie

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ('title', 'description')
    list_display = ['title', 'description']
    search_fields = ('title', 'description')