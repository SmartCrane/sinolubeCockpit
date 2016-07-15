from django.conf.urls import patterns, include, url
from django.conf.urls.shortcut import urlpatterns
from django.contrib import admin

from cockpit import views


urlpatterns += patterns('',
    url(r"^$",views.index),
    url(r"^sub/$",views.sub),
    )


