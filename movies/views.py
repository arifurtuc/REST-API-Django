from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData


# Define a ViewSet for MovieData objects
class MovieViewsSet(viewsets.ModelViewSet):
    # Define the queryset to retrieve all MovieData
    queryset = MovieData.objects.all()

    # Specify the serializer class to be used
    serializer_class = MovieSerializer


# Define a ViewSet for specific MovieData objects based on movie type
class ActionMovieViewsSet(viewsets.ModelViewSet):
    # Define the queryset to retrieve MovieData for specific type
    queryset = MovieData.objects.filter(movie_type='action')

    # Specify the serializer class to be used
    serializer_class = MovieSerializer


# Define a ViewSet for specific MovieData objects based on movie type
class ComedyMovieViewsSet(viewsets.ModelViewSet):
    # Define the queryset to retrieve MovieData for specific type
    queryset = MovieData.objects.filter(movie_type='comedy')

    # Specify the serializer class to be used
    serializer_class = MovieSerializer
