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

**[polls.views.py]**

```python
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 발행일 기준으로 순서대로 정렬되어 있는 Question 테이블의 리스트를 5개 발췌
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    # render() 은 첫번째 인자로서 request 객체를 취한다. 두번째 인자는 template 의 이름, 세번째 인자는 딕셔너리이다.
    # context 와 함께 걸러진 template 의 HttpResponse 객체를 반환한다.

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # 만약에 요청된 ID에 대한 question 이 존재하지 않으면 view 는 Http404 예외를 일으킨다.

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # 모델의 관리자인 get_object_or_404()의 인자는 만약 객자가 존재하지 않으면 Http404를 일으킨다.
    # 왜 DoesNotExist 예외처리를 안 하고 get_object_or_404()를 쓸까? 그 까닭은 장고 중요한 목표의 하나는 느슨한 결합을 유지하는 것이다.
    # 몇 몇의 제어된 결합은 django.shortcuts 모듈에서 도입된다.


def vote(request, question_id):
    def vote(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        print('hi')
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
            # requst.POST['choice'] 는 선택된 choice의 ID 값을 string 으로  반환한다. request.POST value는 항상 string 형이다.
            print('hello')
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # choice count 를 증가시킨 후에 코드는 HttpResponseRedirect 를 반환한다.
            # HttpResponseRedirect 는 한 개의 인자(사용자에게 재반응하여 보여주는 URL)만 취한다.
            # POST 형식으로 전달한 뒤에 항상 HttpResponseRedirect 로 반환되어야한다. 장고라서가 아니라 웹 개발의 좋은 관행이다.

            return HttpResponseRedirect(reverse('results', args=(question.id,)))
    # reverse() 는 이 예제에서 HttpResponseRedirect 생성자에 대해 사용된 것이다.
    # 이 함수는 view 함수에 대응한 URL이 hardcode 하는 것을 피하도록 해준다.
    # 우리가 제어를 통과하고 URL pattern의 다양한 부분에 대한 뷰 함수의 이름을 고려한다.


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
```
<br><br>

**[polls/urls.py]**

```python
from django.conf.urls import url
from . import views # from polls import views


urlpatterns = [
  url(r'^$', views.index, name='index'),
  # the 'name' value as called by the \{\% url \%\} template tag

  url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

  url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

  url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
```

**[polls/index.html]**
```python
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <!--<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>-->
        <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

**[polls/detail.html]**
```python
<h1>{{ question.question_text }}</h1>
{% if error_message %}
    <p><strong>{{ error_message }}</strong></p>
{% endif %}
<form action="{% url 'vote' question.id %}" method="post">
<!-- 이름 인자를 polls.urls.py의 url()에서 정의했기 때문에, -->
<!-- {%  url %} 템플릿 태그를 사용함으로써 url 설정에 정의된 특정한 URL 경로에 대한 의존을 제거할 수 있다. -->
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
{% endfor %}
<input type="submit" value="Vote" />
</form>
```
