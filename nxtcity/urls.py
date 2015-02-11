from django.conf.urls import patterns, include, url
from django.contrib import admin
import landing.views as landing

urlpatterns = patterns('',
    url(r'^/?$', landing.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
