# Task urls
from django.conf.urls import patterns, url
from . import views


urlpatterns = [
	url(r'^$', views.home, name="home"),
	url(r'^api/tasks/$', views.task_collection, name='task_collection'),
	url(r'^api/tasks/(?P<pk>[0-9]+)$', views.task_element,name='task_element'),
]

