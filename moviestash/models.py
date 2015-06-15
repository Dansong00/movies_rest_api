from django.db import models

class Movie(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, default='')
	studio = models.CharField(max_length=100, default='')
	director = models.CharField(max_length=100, default='')
	producer = models.CharField(max_length=100, default='')
	genre = models.CharField(max_length=100, default='')

	class Meta:
		ordering = ('title',)