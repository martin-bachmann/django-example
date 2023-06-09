from django.urls import path

# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import MovieListAV, MovieDetailsAV

urlpatterns = [
    path("list/", MovieListAV.as_view(), name="movie_list"),
    path("<int:pk>", MovieDetailsAV.as_view(), name="movie_detail"),
]
