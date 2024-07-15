from django.db import models
from board.models import Movie
# Create your models here.


class Actor(models.Model):
    movies = models.ForeignKey(Movie,null=True,on_delete=models.CASCADE,related_name="movies")
    name = models.CharField(max_length=255)
    character = models.CharField(max_length=255)
    image_url = models.URLField()
    
    def __str__(self):
        return self.name