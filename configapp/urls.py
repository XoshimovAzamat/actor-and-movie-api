from django.contrib import admin
from django.urls import path
from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieCreateView, ActorCreateView, MovieViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')

urlpatterns = [
    path('movies/create/', MovieCreateView.as_view(), name='movie-create'),
    path('actors/create/', ActorCreateView.as_view(), name='actor-create'),
    path('', include(router.urls)),
]

# urlpatterns = [
# movie get, post
# path('movie_api/', MovieApi.as_view()),
# path('movie_api/<slug:slug>/', MovieDetailApi.as_view()),
# actor get, post
# path('actor_api/', actor_api),
# movie get, put, patch
# path('movie_detail/<slug:slug>', movie_detail),
# actor get, put, patch
# path('actor_detail/<slug:slug>', actor_detail),
# path('ism_api/', ism_api_api),
# ]
