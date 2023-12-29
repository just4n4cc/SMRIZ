from django.contrib import admin
from django.contrib.messages import api
from django.urls import path, include
from . import views
from dotenv import load_dotenv
import os
import subprocess


def get_api_prefix():
    # res = subprocess.run(['git rev-parse --abbrev-ref HEAD | grep dev'])
    res = subprocess.call('git rev-parse --abbrev-ref HEAD | grep dev > /dev/null', shell=True)
    if res == 0:
        return 'dev/'
    return ''


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('film', include('films.urls')),
    path(get_api_prefix() + 'api/', include('films.urls'))
]
