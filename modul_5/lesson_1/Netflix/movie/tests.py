from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Movie
from .serializers import MovieSerializer


class MovieViewSetTests(APITestCase):

    def setUp(self):
        pass

    def test_list_movies(self):
        url = reverse('movies-list')

        response = self.client.get(url, format='json')

        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, serializer.data)

    def test_search_movies(self):
        url = reverse('movies-list')

        response = self.client.get(url, {'search': 'somemovie'}, format='json')

        movies = Movie.objects.filter(name__icontains='somemovie')
        serializer = MovieSerializer(movies, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, serializer.data)

    def test_order_movies_by_imdb(self):
        url = reverse('movies-list')

        response = self.client.get(url, {'ordering': 'imdb'}, format='json')

        movies = Movie.objects.order_by('imdb')
        serializer = MovieSerializer(movies, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, serializer.data)
