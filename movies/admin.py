from django.contrib import admin
from .models import MovieData


# Customizing the MovieDataAdmin to enhance the Django admin interface
class MovieDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'rating')
    search_fields = ('name', )


# Register the MovieData model
admin.site.register(MovieData, MovieDataAdmin)
