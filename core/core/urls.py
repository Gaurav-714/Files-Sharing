from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('download/<uid>', download),
    path('file-upload/', HandleFileUplaod.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()