## Models
모델은 확정적인 데이터 정보 소스의 독보적인 존재입니다. 필수적인 필드를 포함하고 당신이 저장한 데이터를 대표합니다.
각각의 모델은 싱글 데이터베이스 테이블을 매핑합니다.
##### 기본 사항들
- 각각의 모델은 **django.db.models.Model** 을 하위로 삼는 파이썬 클래스입니다.
- 모델의 속성들은 데이터베이스 필드를 나타냅니다.
- 장고는 당신에게 자동으로 생성된 데이터베이스 API를 제공합니다.

> 다음 모델은 **first_name** 과 **last_name** 을 가진 **Person** 을 나타낸 것입니다.

```python
from django.db import models

class Person(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
```

- **first_name** 과 **last_name** 은 모델의 필드입니다. 각각의 필드는 클래스 속성으로 구분되어지고, 속성은 데이터베이스 컬럼으로부터 매핑을 합니다.
- 위 코드를 SQL로 작성한다면 아래와 같았을거에요.

```python
CREATE TABLE myapp_person (
  "id" serial NOT NULL PRIMARY KEY,
  "first_name" varchar(30) NOT NULL,
  "last_name" varchar(30) NOT NULL,
)
```
> 주목 (-ω-ゞ
- myapp(테이블명)의 이름은 모델 메타데이터로부터 자동으로 얻지만 오버라이드 될 수 있습니다.
- 'id' 필드는 자동으로 추가되지만 이 역시 오버라이드 될 수 있습니다.

<br>
### Using models
- 모델을 정의하자마자 당신은 장고에게 이 모델을 사용하려고한다는 것을 알려줘야해요.
- settings 파일의 **INSTALLED_APP** 에서 포함하고자하는 모듈의 이름을 추가합니다.

```python
INSTALLED_APPS = [
  ...
  'myapp',
]
```

> (╭☞•́⍛•̀)╭☞ 깨알 Tip <br>
shell 실행 시, 필요한 모듈 자동 import, 입력어 자동 완성 기능 추가<br>
\#1. pip install django_extensions<br>
\#2. pip install ipython<br>
\#3. settins.py INSTALLED_APP 에 django_extensions 등록<br>
\#4. ./manage.py shell_plus
