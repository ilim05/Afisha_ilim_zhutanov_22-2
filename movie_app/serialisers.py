from rest_framework import serializers
from movie_app.models import Director, Movie, Review

class DirectorSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name']

class MovieSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'duration', 'director']

class ReviewSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'movie']