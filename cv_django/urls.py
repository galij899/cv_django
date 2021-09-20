from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('cv.urls')),
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('i18n/', include('django.conf.urls.i18n'))
]
