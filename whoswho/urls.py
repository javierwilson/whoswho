"""whoswho URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import *

from model_report import report
report.autodiscover()

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^login/$', home),
    url(r'^$', index, name='index'),
    url(r'^group/add$', add_group, name='add_group'),
    url(r'^contact/add$', add_contact, name='add_contact'),
    url(r'^contact/(?P<pk>\d+)/edit$', edit_contact, name='edit_contact'),
    url(r'^contact/(?P<pk>\d+)/view$', single_contact, name='single_contact'),
    url(r'^event/(?P<pk>\d+)/view$', single_contact, name='single_event'),
    url(r'^contact/download$', download_vcard, name='download_vcard'),
    url(r'^reports/', include('model_report.urls')),
]
