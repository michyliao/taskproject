# Task urls
from django.conf.urls import patterns, url
from . import views



# urlpatterns = patterns(
#     'task.views',
#     url(r'^$', 'home'),


#     # api
#     url(r'^api/tasks/$', 'task_collection'),
#     url(r'^api/tasks/(?P<pk>[0-9]+)$', 'task_element')
# )


urlpatterns = [
	url(r'^$', views.home, name="home"),
	url(r'^api/tasks/$', views.task_collection, name='task_collection'),
	url(r'^api/tasks/(?P<pk>[0-9]+)$', views.task_element,name='task_element'),
]



# url(r'^admin/', admin.site.urls),
#     url(r'^index/$', index_view, name="main-view"),