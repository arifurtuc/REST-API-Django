from django.db import models


# Define a Django Model to represent movie data in the database.
class MovieData(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    movie_type = models.CharField(max_length=200, default='action')

    def __str__(self):
        return self.name
