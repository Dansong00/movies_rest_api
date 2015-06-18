from django.shortcuts import render
from moviestash.models import Movie
from moviestash.serializer import MovieSerializer
from rest_framework import generics, permissions

#List all movies and add movies
class MovieList(generics.ListCreateAPIView):
	serializer_class = MovieSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def get_queryset(self):
		queryset = Movie.objects.all()
		return Movie.objects.filter(owner=user)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

#Get a movie and delete a movie
class MovieDetail(generics.RetrieveDestroyAPIView):
	permission_classes =(permissions.IsAuthenticated,)
	serializer_class = MovieSerializer

	def get_queryset(self):
		user = self.request.user
		queryset = Movie.objects.filter(owner=user)