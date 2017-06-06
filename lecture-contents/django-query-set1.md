Use this command
`python manage.py shell`

`<app-name>/models.py`
```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```
`django shell`
```python
>>> from <app-name>.models import Question. Choice

>>> Question.pbjects.all()
<QuerySet []> # 아직 Question 테이블에 어떠한 내용도 없다.

>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
# Question 클래스(테이블) question_text 컬럼에 "What's new", pub_date 컬럼에 settings에 지정해놓은 시간의 값을 추가하고, q에 할당한다.

>>> q.save() # 할당한 내용을 저장.
>>> q.id
1
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetie(...)

>>> q.question_text = "What's up?"
>>> q.save()
# q에 할당된 question_text 내용 변경
# q라는 지정 변수, 즉 가리키는 주소값에 변화를 준 것이기 때문에 내용이 추가된 것이 아니라 단지 변경된다.

>>> Question.objects.all()
# Question 객체를 참조하는 모든 내용 반영
```

`<app-name>/models.py`
```python
from django.db import models
from django.utils.encoding import

class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
'''
  >>> from polls.models import * <br>
  >>> Question.objects.all() <br>
  <QuerySet [<Question: What's up?>]> <br>
'''
  # 안 했을 시, <QuerySet []> 으로 표현된다.
```
