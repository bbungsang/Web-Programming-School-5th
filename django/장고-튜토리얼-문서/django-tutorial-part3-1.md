## Overview
- `view`는 장고 어플리케이션에서 특정한 함수와 특정한 템플릿을 가지는 웹 페이지의 형태이다.

- 이번 투표 어플리케이션에서는 4개의 `view`가 있다.
  - Question 에 대한 `index(메인페이지)` 구현 함수 \- 최근 기재된 순서로 질문 목록들을 나타낸다.
  - Question 에 대한 `detail` 페이지 구현 함수 \- 투표에 대한 양식만 있는, 즉 질문과 선택지를 나타낸다.
  - Question 에 대한 `result` 페이지 구현 함수 \- 질문에 대한 결과를 나타낸다.
  - 투표를 할 수 있는 함수 \- 투표를 처리한다.

- 장고에서 웹 페이지와 기타 내용을 `view`를 통해 구현한다. 각각의 `view`는 간단한 파이썬 함수로 표현된다.

- 장고는 요청된 URL을 검사함으로써 `view`를 선택하며, URL 패턴은 대략 `/polls(앱명)/detail(기능을 지칭)/26(페이지 번호)/...` 이러한 형태를 띈다.

- URL 에서 `view` 를 얻기 위해 장고는 'URLconfs'를 사용한다. 이는 `view`에 대한 URL 패턴을 매핑한다.
<br><br>

#### \# index
**[polls/views.py]**
```python
from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 발행일 기준으로 순서대로 정렬되어 있는 Question 테이블의 리스트를 5개 발췌
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
```
- `render()` 은 첫번째 인자로서 request 객체를 취한다. 두번째 인자는 template 의 이름, 세번째 인자는 딕셔너리이다.
- context 와 함께 걸러진 template 의 HttpResponse 객체를 반환한다.

**[polls/urls.py]**
```python
from django.conf.urls import url
from . import views # from polls import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
```
- name 의 value(index) 는 `{% url %}`로 템플릿의 태그에 쓰인다.

**[polls/index.html]**
```python
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```
<br><br>

#### \#detail
**[polls/views.py]**
```python
from django.shortcuts import get_object_or_404, render

from .models import Choice, Question

...

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # 만약에 요청된 ID에 대한 question 이 존재하지 않으면 view 는 Http404 예외를 일으킨다.

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```
- 모델의 관리자인 get_object_or_404()의 인자는 만약 객자가 존재하지 않으면 Http404를 일으킨다.
- 왜 DoesNotExist 예외처리를 안 하고 get_object_or_404()를 쓸까? 그 까닭은 장고 중요한 목표의 하나는 느슨한 결합을 유지하는 것이다.
- 몇 몇의 제어된 결합은 django.shortcuts 모듈에서 도입된다.

**[polls/urls.py]**
```python
```python
from django.conf.urls import url
from . import views # from polls import views

urlpatterns = [
...
  url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
]
```

**[detail.html]**
```python
<h1>{{ question.question_text }}</h1>
{% if error_message %}
    <p><strong>{{ error_message }}</strong></p>
{% endif %}
<form action="{% url 'vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
{% endfor %}
<input type="submit" value="Vote" />
</form>
```
- 이름 인자를 polls.urls.py 에서 정의했기 떄문에, {%  url %} 템플릿 태그를 사용함으로써 url 설정에 정의된 URL 경로에 대한 의존을 제거할 수 있다.
