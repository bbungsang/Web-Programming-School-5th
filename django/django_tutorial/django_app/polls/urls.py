from django.conf.urls import url
from . import views # from polls import views


urlpatterns = [
    url(r'^$', views.index, name='index'),

    # the 'name' value as called by the {% url %} template tag
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    ]
