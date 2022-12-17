from django.urls import path
from movie_app.views import (directors_view, director_view, movies_view, movie_view, reviews_view, review_view)
urlpatterns = [
    path('directors/', directors_view),
    path('directors/<int:id>/', director_view),
    path('movies/', movies_view),
    path('movies/<int:id>/', movie_view),
    path('reviews/', reviews_view),
    path('reviews/<int:id>/', review_view)
]