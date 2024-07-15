# # serializers.py

# from rest_framework import serializers
# from .models import Movie, Actor, MovieActor

# class ActorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Actor
#         fields = ['name', 'character', 'image_url']

# class MovieActorSerializer(serializers.ModelSerializer):
#     actor = ActorSerializer()

#     class Meta:
#         model = MovieActor
#         fields = ['actor']

# class MovieSerializer(serializers.ModelSerializer):
#     actors = serializers.SerializerMethodField()

#     class Meta:
#         model = Movie
#         fields = [
#             'title_kor', 'title_eng', 'poster_url', 'genre', 'showtime', 
#             'release_date', 'plot', 'rating', 'director_name', 'director_image_url', 'actors'
#         ]

#     def get_actors(self, obj):
#         movie_actors = MovieActor.objects.filter(movie=obj)
#         return MovieActorSerializer(movie_actors, many=True).data










from rest_framework import serializers
from .models import Movie
from member.models import Actor
from .models import Movie




class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['movies', 'name', 'character', 'image_url']





class MovieSerializer(serializers.ModelSerializer):
    # actors = ActorSerializer(many=True)
    # actors= serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = [
            'title_kor', 'title_eng', 'poster_url', 'genre', 'showtime', 
            'release_date', 'plot', 'rating', 'director_name', 'director_image_url'
        ]


    # def create(self, validated_data):
    #     actors_data = validated_data.pop('actors')
    #     movie = Movie.objects.create(**validated_data)
    #     for actor_data in actors_data:
    #         actor, created = Actor.objects.get_or_create(**actor_data)
    #         movie.actors.add(actor)
    #     return movie


        

from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.profile.nickname', read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'nickname', 'title', 'body', 'created_at']
        extra_kwargs = {
            'user': {'read_only': True}
        }

class CommentSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.profile.nickname', read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'nickname', 'comment', 'created_at']
        extra_kwargs = {
            'user': {'read_only': True}
        }
