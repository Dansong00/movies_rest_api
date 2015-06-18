
from rest_framework import serializers
from moviestash.models import Movie
 
 
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'studio', 'producer', 'director')

