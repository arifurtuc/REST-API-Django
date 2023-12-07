from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData


# Define a ViewSet for MovieData objects
class MovieViewsSet(viewsets.ModelViewSet):
    # Define the queryset to retrieve all MovieData
    queryset = MovieData.objects.all()

    # Specify the serializer class to be used
    serializer_class = MovieSerializer
