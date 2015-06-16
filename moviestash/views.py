from django.shortcuts import render
from moviestash.models import Movie
from moviestash.serializer import MovieSerializer
from rest_framework import generics

#List all movies and add movies
class MovieList(generics.ListCreateAPIView):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer

#Get a movie and delete a movie
class MovieDetail(generics.RetrieveDestroyAPIView):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer