## Models
모델은 확정적인 데이터 정보 소스의 독보적인 존재입니다. 필수적인 필드를 포함하고 당신이 저장한 데이터를 대표합니다.
각각의 모델은 싱글 데이터베이스 테이블을 매핑합니다.
##### 기본 사항들
- 각각의 모델은 **django.db.models.Model** 을 하위로 삼는 파이썬 클래스입니다.
- 모델의 속성들은 데이터베이스 필드를 나타냅니다.
- 장고는 당신에게 자동으로 생성된 데이터베이스 API를 제공합니다.

> 다음 모델은 **first_name** 과 **last_name** 을 가진 **Person** 을 나타낸 것이다.

```python
from django.db import models

class Person(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
```

- **first_name** 과 **last_name** 은 모델의 필드입니다. 각각의 필드는 클래스 속성으로 구분되어지고, 속승은 데이터베이스 컬럼으로부터 매핑을 합니다.
