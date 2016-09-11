from django.conf.urls import url

from . import views

app_name = 'poem'
urlpatterns = [
    url(r'^(?P<curr_poem>.*)$', views.detail, name='detail'),
]
