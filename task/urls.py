# Task urls
from django.conf.urls import patterns, url
from . import views



urlpatterns = patterns(
    'task.views',
    url(r'^$', 'home'),


    # api
    url(r'^api/tasks/$', 'task_collection'),
    url(r'^api/tasks/(?P<pk>[0-9]+)$', 'task_element')
)
