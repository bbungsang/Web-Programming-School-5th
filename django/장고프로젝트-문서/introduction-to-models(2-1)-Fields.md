# Fields
- `Fields`는 모델에서 가장 중요한 부분입니다. 또한 모델에서만 요구되어집니다.
- `Fields`는 정의한 데이터베이스 필드의 리스트이며, 클래스의 속성들로 구성되어있습니다. **clean, save, delete** 와 같이 충돌되는 필드 이름을 선택하지 않도록 주의하세요.

[Example]

```python
from django.db import models

class Musician(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  instrument = models.CharField(max_length=100)

class Album(models.Model):
  artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  release_date = models.DateTimeField()
  num_stars = models.IntegerField()
```
#### Field types
각각의 필드는 필드 클래스의 인스턴스가 되야합니다. 그러므로 장고는 몇 가지 사항을 필드 클래스로 사용합니다.
1. 저장된 데이터의 종류가 무엇인지 알도록 하는 `Column Type`(INTEGER, VARCHAR, TEXT)
2. 폼을 렌더링할 때 사용하는 `기본 HTML 위젯`(input type="text">, <select>)
3. 장고 관리자와 자동으로 제공되는 폼에서 사용되는 `Minimal Validation Requirements`
<br>

#### Field options
필드는 특정한 인자를 가집니다. 예를 들어, **CharField** 는 데이터를 저장할 때 사용되는 **VARCHAR** 의 크기에 대한 **max_length** 인자를 요구합니다.

##### 모든 필드 타입에서 사용할 수 있는 common arguments
**null**
- True면 장고는 빈 값을 NULL값으로서 데이터베이스에 저장할 것입니다. Default는 False.

**blank**
- True면 필드는 공백이 허용됩니다. Default는 Flase.

> 주목 (-ω-ゞ <br>
`null 과 blank 는 다릅니다.`<br>
null은 순전히 데이터베이스 관련 개념이고, blank는 식별(?) 관련 개념입니다. 즉, blank는 값이 인정되지만 식별함에 있어서 공백인 것입니다. 만약 필드가 **blank=True** 라면, 폼 검사에서 빈 값의 제출을 허용할 것이고, **blank=False** 면, 해당 필드는 값이 요구되어질 것입니다.

**choices**
- 필드에 2개의 튜플을 사용하는 것으로 Default 폼 위젯은 기본 텍스트 필드를 대신해서 선택 상자가 될 것이고 그 한계는 choices를 준 만큼입니다.

```python
from django.db import models

class Person(models.Model):
  SHIRT_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),    
  )
  name = models.CharField(max_length=60)
  shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
```
- 튜플의 첫번째 요소는 데이터베이스에 저장될 값입니다. 두번째 요소는 Default 폼 위젯 혹은 ModelchoiceField에 보여질 것입니다. choices 필드의 보여지는 값은 `get_FOO_display()`로 접근할 수 있습니다.

```python
>>> p = Person(name="Elena Kim", shirt_size="M")
>>> p.save()
>>> p.shirt_size
'L'
>>> p.get_shirt_size_display()
'Large'
```

**default**
- 디폴트 값은 매번 새로 생성되는 객체를 호출하는 하나의 값이거나 callable object일 수 있습니다.

**primary_key**
- **priamry_key=True** 면 이 필드가 기본키인 것입니다.
- 하지만 **priamry_key=True** 를 인자로 주지 않더라도 장고는 자동으로 기본키를 int 타입으로 추가시킵니다.
- 기본키인 필드는 읽기 전용이며, 기본키값을 바꿨더라도 새로운 객체는 이전의 규칙을 따라서 생성될 것입니다.

```python
from django.db import models

class Fruit(models.Model):
  name = models.CharField(max_length=100, primary_key=True)
```
```python
>>> fruit = Fruit.objects.create(name='Apple')
>>> fruit.name = 'Pear'
>>> fruit.save()
>>> Fruit.objects.values_list('name', flat=True)
['Apple', 'Pear']
```
**unique**
- True면, 이 필드는 테이블의 모든 항목에서 반드시 유일해야햡니다.
