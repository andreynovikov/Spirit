#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns("spirit.views.topic_poll",
    url(r'^update/(?P<pk>\d+)/$', 'poll_update', name='poll-update'),
)