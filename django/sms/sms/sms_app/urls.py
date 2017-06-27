from django.conf.urls import url

from sms_app import views

app_name = 'sms_app'
urlpatterns = [
    url(r'^$', views.sms_send, name='sms_send'),
    url(r'^(?P<sms_pk>\d+)/result/$', views.sms_result, name='sms_result')
]