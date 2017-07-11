from django.conf.urls import url, include

from . import urls_views, urls_apis

urlpatterns = [
    # urls_views 를 포함하여 일반 url 을 나타낸다.
    url(r'^', include(urls_views)),

    # urls_apis 를 포함아여 api/post 형식으로 GET 접근하면, 해당 페이지가 표시하는 데이터를 얻을 수 있다.
    url(r'^api/', include(urls_apis)),
]