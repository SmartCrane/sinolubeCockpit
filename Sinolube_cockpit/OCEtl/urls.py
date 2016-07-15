from django.conf.urls import patterns, include, url
from django.conf.urls.shortcut import urlpatterns
from django.contrib import admin

from OCEtl import views


urlpatterns = patterns('',
    # url(r"^$",views.getorderstatics),
    url(r"^$",views.getorderstatics),
    )