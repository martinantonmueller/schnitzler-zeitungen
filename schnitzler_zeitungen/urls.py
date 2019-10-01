from django.conf.urls import url, include, handler404
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('webpage.urls', namespace='webpage')),
]


handler404 = 'webpage.views.handler404'
