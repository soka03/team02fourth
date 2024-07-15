from django.db import models
from django.db import models
from member.models import CustomUser

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='board_posts')
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='board_comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


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
