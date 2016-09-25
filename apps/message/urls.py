from django.conf.urls import url

from apps.message.views import wall
from apps.message.views import add

app_name = 'message'
urlpatterns = [
    url(r'^$', wall),
    url(r'^add/$', add, name='add'),
]
