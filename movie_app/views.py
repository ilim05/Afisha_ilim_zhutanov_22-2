from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Director, Review, Movie
from movie_app.serialisers import DirectorSeriaLizer, ReviewSeriaLizer, MovieSeriaLizer

@api_view(['GET'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSeriaLizer(directors, many=True)
        return Response(data=serializer.data)


@api_view(['GET'])
def director_view(request, **kwargs):
    if request.method == 'GET':
        director = Director.objects.get(id=kwargs['id'])
        serializer = DirectorSeriaLizer(director, many=False)
        return Response(data=serializer.data)

@api_view(['GET'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSeriaLizer(movies, many=True)
        return Response(data=serializer.data)

@api_view(['GET'])
def movie_view(request, **kwargs):
    if request.method == 'GET':
        movie = Movie.objects.get(id=kwargs['id'])
        serializer = MovieSeriaLizer(movie, many=False)
        return Response(data=serializer.data)

@api_view(['GET'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSeriaLizer(reviews, many=True)
        return Response(data=serializer.data)

@api_view(['GET'])
def review_view(request, **kwargs):
    if request.method == 'GET':
        review = Review.objects.get(id=kwargs['id'])
        serializer = ReviewSeriaLizer(review, many=False)
        return Response(data=serializer.data)