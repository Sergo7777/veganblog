from django.conf.urls import url
from django.contrib import admin

from .views import(
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    post_map,
    category,
)
urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^category/(?P<id>[0-9]{1})/$', category, name='category'),
    url(r'^create/$', post_create, name='create'),
    url(r'^map/$', post_map, name='map'),
    url(r'^(?P<slug>[\w\-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w\-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', post_delete, name='delete'),
]