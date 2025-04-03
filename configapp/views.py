from .models import *
from .serializers import *
from rest_framework.generics import CreateAPIView
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import MovieSerializer, ActorSerializer


class MovieCreateView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ActorCreateView(generics.CreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=['post'])
    def add_actor(self, request, pk=None):
        movie = self.get_object()
        actor_id = request.data.get("actor_id")
        actor = get_object_or_404(Actor, id=actor_id)
        movie.actor.add(actor)
        return Response({"message": "Actor added successfully"}, status=status.HTTP_200_OK)


# class MovieApi(APIView):
#
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         data = {'success': True}
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             data['serializer'] = serializer.data
#             return Response(data=data)
#         data['success'] = False
#         return Response(data=data)
#
# class MovieDetailApi(APIView):
#     def get(self, request, slug):
#         response = {'success':True}
#         try:
#             movie = Movie.objects.get(slug=slug)
#             serializer = MovieSerializer(movie)
#             response["data"]=serializer.data
#             return Response(data=response)
#         except Movie.DoesNotExist:
#             response["success"] = False
#             return Response(data=response)
# #
# @api_view(["GET", "POST"])
# def movie_api(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     if request.method == "POST":
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(["GET", "POST"])
# def actor_api(request):
#     if request.method == "GET":
#         actors = Actors.objects.all()
#         serializer = ActorSerializer(actors, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     if request.method == "POST":
#         serializer = ActorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(["GET", "PUT", "PATCH", "DELETE"])
# def movie_detail(request, slug):
#     try:
#         movie = Movie.objects.get(slug=slug)
#     except Movie.DoesNotExist:
#         return Response(
#             data={"status": False, "error": "Movie not found"},
#             status=status.HTTP_404_NOT_FOUND
#         )
#
#     if request.method == "GET":
#         serializer = MovieSerializer(movie)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == "PUT":
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "PATCH":
#         serializer = MovieSerializer(movie, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "DELETE":
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(["GET", "PUT", "PATCH", "DELETE"])
# def actor_detail(request, slug):
#     try:
#         actor = Actors.objects.get(slug=slug)
#     except Actors.DoesNotExist:
#         return Response(
#             data={"status": False, "error": "Actor not found"},
#             status=status.HTTP_404_NOT_FOUND
#         )
#
#     if request.method == "GET":
#         serializer = ActorSerializer(actor)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == "PUT":
#         serializer = ActorSerializer(actor, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "PATCH":
#         serializer = ActorSerializer(actor, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "DELETE":
#         actor.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['POST'])
# def ism_api(request):
#     try:
#         ism = request.data['ism']
#         fam = request.data['fam']
#         yil = request.data['yil']
#         return Response(data={'message': f'Salom {fam} {ism}, yili: {yil}'})
#     except KeyError as e:
#         return Response(
#             data={'error': f'Majburiy maydon yetishmayapti: {str(e)}'},
#             status=status.HTTP_400_BAD_REQUEST
#         )
