from rest_framework import serializers
from .models import MovieData


# Define a serializer for the MovieData model to convert model instances
# into JSON data
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieData
        # Specify the fields to be included in the serialized representation
        fields = ['id', 'name', 'duration', 'rating', 'movie_type']
