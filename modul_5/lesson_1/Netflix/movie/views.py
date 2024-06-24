from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Movie, Actor, Comment
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import ActorSerializer, MovieSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.decorators import action


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='add-actor')
    def add_actor(self, request):
        movie_id = request.query_params.get('movie_id')
        actor_id = request.query_params.get('actor_id')

        if not movie_id or not actor_id:
            return Response({"error": "movie_id and actor_id are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            movie = Movie.objects.get(pk=movie_id)
            actor = Actor.objects.get(pk=actor_id)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        except Actor.DoesNotExist:
            return Response({"error": "Actor not found"}, status=status.HTTP_404_NOT_FOUND)

        movie.actors.add(actor)
        return Response({"message": "Actor added to movie"}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['delete'], url_path='remove-actor')
    def remove_actor(self, request):
        movie_id = request.query_params.get('movie_id')
        actor_id = request.query_params.get('actor_id')

        if not movie_id or not actor_id:
            return Response({"error": "movie_id and actor_id are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            movie = Movie.objects.get(pk=movie_id)
            actor = Actor.objects.get(pk=actor_id)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        except Actor.DoesNotExist:
            return Response({"error": "Actor not found"}, status=status.HTTP_404_NOT_FOUND)

        movie.actors.remove(actor)
        return Response({"message": "Actor removed from movie"}, status=status.HTTP_201_CREATED)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class MovieActorAPIView(APIView):
    def get(self, request, id):
        try:
            movie = Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

        actors = movie.actors.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id

        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentDeletApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        comment = get_object_or_404(Comment, pk=id)
        if comment.user != request.user:
            return Response({"error": "You do not have permission to delete this comment"},
                            status=status.HTTP_403_FORBIDDEN)

        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
