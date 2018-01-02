"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/

"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

from web import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    #url(r'^', lambda req: render(req, 'index.html')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

