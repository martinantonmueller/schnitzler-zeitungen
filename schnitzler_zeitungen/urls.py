from django.conf.urls import url, include, handler404
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('webpage.urls', namespace='webpage')),
    url(r'^transkribus/', include('transkribus.urls', namespace='transkribus')),
]


handler404 = 'webpage.views.handler404'
