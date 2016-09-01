from .models import Sport, Athlete
from rest_framework import serializers


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ('name', 'icon', 'description',)


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = (
            'first_name',
            'last_name',
            'birth_place',
            'birthdate',
            'age',
            'weight',
            'height',
            'coach_name',
            'video',
            'sport',
            'photo',
        )
