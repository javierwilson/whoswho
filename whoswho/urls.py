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

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^login/$', home),
    url(r'^$', index, name='index'),
    url(r'^group/add$', add_group, name='add_group'),
    url(r'^contact/add$', add_contact, name='add_contact'),
    url(r'^contact/(?P<pk>\d+)/edit$', edit_contact, name='edit_contact'),
    url(r'^contact/(?P<pk>\d+)/view$', single_contact, name='single_contact'),
    url(r'^group/(?P<name>[\w ]+)/view$', single_group, name='single_group'),
    url(r'^tag/(?P<name>[\w ]+)/view$', single_tag, name='single_tag'),
    url(r'^contact/download$', download_vcard, name='download_vcard'),
]
