from django.db import models
from django.conf import settings
# Create your models here.
class Movie(models.Model):
    poster_path = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    vote_average = models.IntegerField()
    overview = models.TextField()
    release_date = models.CharField(max_length=100)
    movie_id = models.IntegerField()
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name = 'favorite_movies',
    )

class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = 'reviews',
    )
    content = models.TextField()
    rating = models.IntegerField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)


