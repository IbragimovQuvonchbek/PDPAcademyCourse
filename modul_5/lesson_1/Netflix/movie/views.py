from django.shortcuts import render
from rest_framework.response import Response

from .models import Movie, Actor
from .serializers import ActorSerializer, MovieSerializer
from rest_framework.views import APIView


# Create your views here.

class MovieViewSet(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


class ActorViewSet(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)
