## Relationships
- 관계형 데이터베이스의 강점은 서로 관련이 있는 테이블에 있습니다. 장고는 데이터베이스 관계를 정의할 수 있는 3가지 방법을 제공합니다.

#### Many-to-one relationships
- 이 방법을 설명하기 위해 django.db.models.ForeignKey 사용할 것입니다.
- 외래키는 정해진 위치에 클래스형 인자를 요구합니다.
- 예를 들어, `Car` 모델이 `Manufacturer`를 포함한다면, Manufacturer은 다양한 자동차를 만들지만 하나의 Car 객체는 하나의 Manufacturer를 가지게됩니다.

```python
from django.db import models

class Manufacturer(models.Model):
  pass

class Car(models.Model):
  manufacturer = models.ForeignKey(
    Manufacturer,
    on_delete=models.CASCADE
  )
```

#### Many-to-many relationships

#### Extra fields on many-to-many relationships
