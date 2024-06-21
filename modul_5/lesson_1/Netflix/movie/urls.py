from django.urls import path
from .views import MovieViewSet, ActorViewSet

urlpatterns = [
    path('movies/', MovieViewSet.as_view(), name='movies'),
    path('actors/', ActorViewSet.as_view(), name='actors'),
]
