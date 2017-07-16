
## 장고 설치 후, 기본 골격을 만들어주는 스크립트 실행
###### 장고 소스 코드 .py 를 만들고 장고 스타일로 디렉토리를 구성한다는 의미다.
###### \# 모든 작업은 가상환경(virtualenv) 안에서 해야한다.

[맥 OS와 리눅스]
- 명령어 끝에 .(마침표) : 현재 디렉토리에 장고를 설치하라는 표시이다.

> `django-admin startproject <프로젝트명> .`

- 이를 통해 `장고 rule`에 따른 새로운 프로젝트 디렉토리와 파일들을 생성해준다.

```text
djangogirls
├───manage.py -> 사이트 관리를 도와줌, 다른 설치 작업 없이 바로 웹 서버를 시작할 수 있다.
└───mysite
        settings.py -> 웹 설정이 있다.
        urls.py -> urlresolver가 사용하는 패턴 목록 포함, 즉 어디로 자원을 전달해야 하는지 판단한다.
        wsgi.py
        __init__.py
```
- 디렉토리와 파일명 매우 중요 따라서 마음대로 변경하거나 다른 곳으로 옮겨서는 안된다.<br><br>

#### 설정 변경
**[<프로젝트디렉토리>/settings.py]**<br>
현재 장고 프로젝트를 진행하기 위한 기본 설정이 담겨있는 코드이다. 추가적인 설정이 필요하다.

```python
import os
from os.path import abspath, dirname, join

BASE_DIR = join(abspath(__file__), '..', '..')
# __file__ => /home/bbungsang/projects/django_/djangogirls/first_django_project/settings.py
# .. => /home/bbungsang/projects/django_/djangogirls/
# .. => /home/bbungsang/projects/django_/
```

\# 정확한 시간 넣기<br>

> TIME_ZONE = 'Asia/Seoul'<br>
- django 내에서 날짜/시간을 보여주고 저장할 때의 Time Zone

\# 정적파일 경로 추가 <br>

> STATIC_URL = '/static' <br>
> STATIC_ROOT = os.path.join(BASE_DIR, 'static')<br>
- 위와 같이 이 경로는 `/home/bbungsang/projects/django_/static` 을 의미한다.

<br>

#### 데이터베이스 설정

> \# sqlite3 사용 전제
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

<br>

###### 설정이 다 끝났으면 단 *3step* 만으로 웹어플리케이션을 실행할 수 있다.
그 전에 장고에는 2가지의 migration 과정이 있는데, <br>
[manage.py]에서 `makemigration`, `migrate` 이다.

> step1 : 데이터베이스를 생성하기 위해 콘솔 창에서 `python manage.py migrate` 를 실행해야하는데, 이 때, `djangogirs` 디렉토리 안에 있는 `manage.py` 가 필요하다.<br><br>
> step2 : 콘솔창에 `python manage.py runserver` 명령을 실행한다.<br><br>
> step3 : 끝으로, 브라우저에 `http://127.0.0.1:8000/`를 입력하면 아래 이미지와 같이 개발 서버가 뜬다.<br><br>

![it_worked](../images/it_worked.png)
