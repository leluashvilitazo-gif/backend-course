from django.contrib import admin
from .models import Genre, Director, Movie, BoxOffice, Actor, Role

# Register your models here.
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Actor)

class RoleInline(admin.TabularInline):
    model = Role
    extra = 1

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "release_year", "age_rating", "is_published", "director")
    list_filter = ("age_rating", "is_published", "director")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("genres",)
    inlines = [RoleInline]

@admin.register(BoxOffice)
class BoxOfficeAdmin(admin.ModelAdmin):
    list_display = ("movie", "tickets_sold", "gross")