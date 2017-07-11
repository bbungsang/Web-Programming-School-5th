"""make_instargram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

from config import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^post/', include('post.urls.urls_views')),
    url(r'^member/', include('member.urls')),

    url(r'^member/', include('allauth.urls')),

    # rest API 진입점
    # url(r'^rest-api/', include('rest_framework.urls')),9
    # url(r'^rest-swagger/', include('rest_framework_swagger.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
