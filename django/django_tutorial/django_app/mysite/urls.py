"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from polls import urls as polls_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^polls/', include('polls.urls')),
    # polls/ 로 시작하고 그 뒤에는 어떤 내용이 오든 상관이 없으므로 $ 표시가 없음
    # polls 패키지 안에 있는 urls 를 참조한다는 의미
    url(r'^polls/', include(polls_urls)),
]
