from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import MovieViewSet, ActorViewSet, RemoveActorFromAPIView, AddActorToMovieAPIView, MovieActorAPIView, \
    CommentCreateAPIView, CommentListAPIView, CommentDeletApiView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movies', MovieViewSet, 'movies')
router.register(r'actors', ActorViewSet, 'actors')

urlpatterns = [
    path('', include(router.urls)),
    path('movies/<int:id>/actors/', MovieActorAPIView.as_view()),
    path('add-actor/', AddActorToMovieAPIView.as_view()),
    path('remove-actor/', RemoveActorFromAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('comments/', CommentListAPIView.as_view()),
    path('create-comment/', CommentCreateAPIView.as_view()),
    path('delete-comment/<int:id>/', CommentDeletApiView.as_view())
]
