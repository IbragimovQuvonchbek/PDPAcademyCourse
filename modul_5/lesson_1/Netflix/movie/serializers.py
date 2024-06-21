import datetime

from rest_framework import serializers

from .models import Movie, Actor


class ActorSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField()

    def validate_birth_date(self):
        if self.birth_date < datetime.date(1950, 1, 1):
            raise serializers.ValidationError("Birthdate must be on or after 01.01.1950")
        return self.birth_date

    class Meta:
        model = Actor
        fields = ['name', 'birth_date', 'gender']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
