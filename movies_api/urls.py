from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('', 
    # Examples:
    # url(r'^$', 'movies_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^movies/', include('moviestash.urls')),
    url(r'^signin/', include('oauth2_provider.urls', namespace='oauth2_provider')),
)

admin.autodiscover()