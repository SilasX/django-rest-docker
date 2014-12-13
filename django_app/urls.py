from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #API
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    url(r'^api/', include('api.urls', namespace='api'))
)
