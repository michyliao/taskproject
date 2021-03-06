"""taskproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import settings


#heroku static files settings (Reference : http://stackoverflow.com/questions/9047054/heroku-handling-static-files-in-django-app)
if not settings.DEBUG:
    urlpatterns = [
	    url(r'^', include('task.urls')), #include task urls.py
	    url(r'^admin/', admin.site.urls),
    	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    ]
else:
	urlpatterns =[
		url(r'^', include('task.urls')), #include task urls.py
		url(r'^admin/', admin.site.urls),
	]