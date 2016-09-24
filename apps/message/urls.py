from django.conf.urls import url

from apps.message.views import wall

app_name = 'message'
urlpatterns = [
    url(r'^$', wall),
]
