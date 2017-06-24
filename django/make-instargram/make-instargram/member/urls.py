from django.conf.urls import url
from . import views

app_name = 'member'
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^login/$', views.signup, name='signup'),
]