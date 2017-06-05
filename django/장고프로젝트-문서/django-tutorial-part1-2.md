### The development server
- 바깥의 `mysite` 디렉토리로 이동하세요. 만약 이미 그 지점에 있다면 아래와 같이 명령어를 입력해주세요.<br>
> `python manage.py runserver`

- 입력후, `http://127.0.0.1:8000`의 주소를 당신의 브라우저에 입력해보세요. `"Welcome to Django” page, in pleasant, light-blue pastel. It worked!`라는 페이지를 보게될 것입니다.
- 지금 당신은 작업을 할 프로젝트 환경을 설정한 것 입니다.  
- 장고는 어플리케이션의 기본 디렉토리 구조를 자동으로 만드는 유틸리티를 제공합니다. 따라서 당신이 디렉토리들을 만드는 것보다는 코드를 작성하는 것에 초점을 맞추고 있습니다.
- 어플리케이션을 생성하기 위해서 당신은 `manage.py`와 같은 디렉토리의 명령어 입력창에 다음과 같이 입력합니다.<br>

> `python manage.py startapp polls`

- 이러한 레이아웃과 같은 `polls` 디렉토리를 생성할 것입니다.
```python
polls/
  __init__.py
  admin.py
  apps.py
  migrations/
      __init__.py
  models.py
  tests.py
  views.py
```<br><br>

#### 첫번 째 View 작성하기
[polls.views.py]
```python
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello, world. You're at the polls index")
```
- 이것은 장고에서 가장 간단한 뷰 입니다. 뷰를 호출하기 위해서 URL을 매핑해야하는데 여기에서 우리는 URLconf가 필요합니다.
- polls 디렉토리에서 URLconf를 생성하기 위해서 어플리케이션 디렉토리에서 urls.py를 생성하고 다음과 같이 코드를 작성합니다.

[polls/urls.py]
```python
from django.conf.urls import urls

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index')
]
```
- polls.urls 모듈을 root URLconf 로 지정하기 위해 mysite/urls.py 에서 다음과 같이 include()를 삽입해야합니다.

[mysite/urls.py]
```python
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
  url(r'^polls/', include('polls.urls')),
  url(r'^admin/', admin.site.urls),
]
```
- `include()` 함수는 다른 URLconf를 참조하도록 허용합니다. include()를 사용한 url 패턴에서 '/' 다음에 정규표현식 '$'를 사용하지 않았다는 점을 주의하세요.
- 당신이 다른 URL 패턴을 포함시키고자 할 때 항상 include()를 사용하지만 admin.site.urls 는 이에 예외 사항입니다.
