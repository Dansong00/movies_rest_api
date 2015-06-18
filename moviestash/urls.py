from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from moviestash import views

urlpatterns = patterns('',
	url(r'^$', views.MovieList.as_view()),
	url(r'^(?P<pk>[0-9]+)/$', views.MovieDetail.as_view()),
	)

urlpatterns = format_suffix_patterns(urlpatterns)