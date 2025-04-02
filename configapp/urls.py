from django.contrib import admin
from django.urls import path
from configapp.views import movie_api, movie_detail, actor_api, actor_detail
from configapp.views import ism_api

urlpatterns = [
        # movie get, post
        path('movie_api/', movie_api),
        # actor get, post
        path('actor_api/', actor_api),
        # movie get, put, patch
        path('movie_detail/<slug:slug>', movie_detail),
         # actor get, put, patch
        path('actor_detail/<slug:slug>', actor_detail),

    path('ism_api/', ism_api),
]
