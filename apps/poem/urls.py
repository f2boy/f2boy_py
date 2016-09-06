from django.conf.urls import url

from . import views

app_name = 'poem'
urlpatterns = [
    url(r'^$', views.yzyr, name='yzyr'),
]
