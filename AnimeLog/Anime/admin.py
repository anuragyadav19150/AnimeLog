from django.contrib import admin

# Register your models here.
from .models import Anime,Genre
class AnimeAdmin(admin.ModelAdmin):
    list_display = ("ids", "Name", "myRating", "imdbRating","malRating")
    filter_horizontal=("genre",)


admin.site.register(Anime,AnimeAdmin)
admin.site.register(Genre)