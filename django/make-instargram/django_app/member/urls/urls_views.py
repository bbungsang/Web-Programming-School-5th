from django.conf.urls import url
from .. import views

app_name = 'member'
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^allauth_login/$', views.allauth_login, name='allauth_login'),
    url(r'^signup/$', views.signup, name='signup'),
]