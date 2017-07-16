## 장고 모델
> `User` <---> `Django` <---> `DataBase` <br>

- 유저가 데이터를 요청하면, 장고가 앞단에서 데이터를 받아서 데이터베이스에게 전달
- 데이터베이스가 데이터를 꺼내어 응답하면 그 응답을 다시 장고가 유저에게 전달

- 장고 프로젝트는 SQLite3 DB가 기본으로 설정되어 있다. (실 서비스에서는 그다지 적합하지는 않다.)
- 원래 DB Table을 만들고 조회/추가/수정/삭제 하기 위해서는 SQL을 써야만 한다. 하지만 장고가 지원해주는 Django Model을 쓰면, 직접 SQL을 작성하지 않고도 모델을 통해 SQL을 작성할 수 있다.
- 장고 모델은 파이썬 클래스 문법형태로 정의한다.<br><br>

#### 블로그에 어떤 내용을 저장할 것인지 설계하기
Post \# 저장 단위에 대한 이름<br>
------ 속성 ------<br>
title \# 제목<br>
text \# 내용<br>
author \# 작성자<br>
created_date \# 생성날짜<br>
published_date \# 발행날짜 <br><br>

#### 어플리케이션 제작하기
`python manage.py startapp <생성할 앱의 이름>`<br>
manage.py 명령어를 입력할 시, 항상 manage.py 가 있는 디렉토리에서 입력할 것. <br>
어플리케이션을 생성하면 장고에게 사용함을 알려줘야 한다. <br>
[settings.py]
```python
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth', ...
  'blog', # 반드시 ,(콤마)를 붙일것
]
```
[models.py]
```python
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_lenght=200) # 길이 제한 있는 문자열
    text = models.TextField() # 길이 제한 없는 문자열
    created_date = models.DateTimeField(default=timezone.now) # 포스트 생성시 현재 시간이 자동으로 기입된다.
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
```
- 코드를 작성했다고 해서 데이터베이스가 바로 생성되는 것은 아니다. 반드시 마이그레이션 작업을 해야 데이터베이스가 생성된다.
> 모델로부터 마이그레이션 파일을 생성 : `python manage.py makemigrations blog`<br> \# blog 앱을 타겟으로 마이그레이션 맵을 만들겠다는 명령어 <br>
\# 즉, 마이그레이션은 이를 통해 테이블을 어떤식으로 적용할 것인지에 대한 일종의 지시서와 같은 것이다.<br>
마이그레이션 파일을 테이블에 적용 : `python manage.py migrate blog`<br><br>
\# 마이그레이트는 마이그레이션 생성에 전혀 이상이 없으면, 이를 그대로 데이터베이스에 반영하겠다는 뜻이다.
<br><br>

## Django 관리자
[blog/admin.py]
```python
from django.contrib import admin
from .models import Post # 같은 경로의 models.py에서 Post 테이블을 불러옴.

admin.site.register(Post) # 이 등록만으로도 장고에서 모델로 사용할 수 있음.
```
python manage.py runserver `0:9000` : 9000번 포트에서 열겠다는 표현.

슈퍼유저를 생성해야한다. `python manage.py createsuperuser`
