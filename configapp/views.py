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


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def movie_detail(request, slug):
    try:
        movie = Movie.objects.get(slug=slug)
    except Movie.DoesNotExist:
        return Response(
            data={"status": False, "error": "Movie not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def actor_detail(request, slug):
    try:
        actor = Actors.objects.get(slug=slug)
    except Actors.DoesNotExist:
        return Response(
            data={"status": False, "error": "Actor not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        serializer = ActorSerializer(actor)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = ActorSerializer(actor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def ism_api(request):
    try:
        ism = request.data['ism']
        fam = request.data['fam']
        yil = request.data['yil']
        return Response(data={'message': f'Salom {fam} {ism}, yili: {yil}'})
    except KeyError as e:
        return Response(
            data={'error': f'Majburiy maydon yetishmayapti: {str(e)}'},
            status=status.HTTP_400_BAD_REQUEST
        )