from django.conf.urls import url
from apps.wechat.views import verify

app_name = 'wechat'
urlpatterns = [
    url(r'^verify/$', verify, name='verify'),
]
