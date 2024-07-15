from django.db import models


class Movie(models.Model):
    title_kor = models.CharField(max_length=255)
    title_eng = models.CharField(max_length=255)
    poster_url = models.URLField()
    genre = models.CharField(max_length=255)
    showtime = models.CharField(max_length=255)
    release_date = models.DateField()
    plot = models.TextField()
    rating = models.CharField(max_length=10)
    director_name = models.CharField(max_length=255)
    director_image_url = models.URLField()

    def __str__(self):
        return self.title_eng
