from rest_framework import serializers
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(["GET", "POST"])
def movie_api(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def actor_api(request):
    if request.method == "GET":
        actors = Actors.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT", "PATCH", "DELETE"])
def movie_detail(request, slug):
    try:
        movie = Movie.objects.get(slug=slug)

        response = {"status": True}
    except Exception as e:
        response["error"] = e
        return Response(data=response, status=status.HTTP_417_EXPECTATION_FAILED)
    if request.method == "GET":
        serializer = MovieSerializer(movie)
        response["data"] = serializer
        return Response(data=response, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT", "PATCH", "DELETE"])
def actor_detail(request, slug):
    try:
        actor = Actors.objects.get(slug=slug)

        response = {"status": True}
    except Exception as e:
        response["error"] = e
        return Response(data=response, status=status.HTTP_417_EXPECTATION_FAILED)
    if request.method == "GET":
        serializer = ActorSerializer(actor)
        response["data"] = serializer
        return Response(data=response, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = ActorSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        serializer = ActorSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)