from django.conf.urls import patterns, url, include
from assetstorage import views

urlpatterns = patterns('',\
    url(r'^(?P<filename>.+)$', views.asset, name='asset'),
)

