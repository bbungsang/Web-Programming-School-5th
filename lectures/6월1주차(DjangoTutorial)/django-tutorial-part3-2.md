#### \# vote
**[polls/views.py]**
```python
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Choice, Question

...

  def vote(request, question_id):
      question = get_object_or_404(Question, pk=question_id)
      print('hi')
      try:
          selected_choice = question.choice_set.get(pk=request.POST['choice'])

      except (KeyError, Choice.DoesNotExist):
          return render(request, 'polls/detail.html', {
              'question': question,
              'error_message': "You didn't select a choice",
          })
      else:
          selected_choice.votes += 1
          selected_choice.save()

          return HttpResponseRedirect(reverse('results', args=(question.id,)))
```
- requst.POST['choice'] 는 선택된 choice의 ID 값을 string 으로  반환한다. request.POST value는 항상 string 형이다.
- choice count 를 증가시킨 후에 코드는 HttpResponseRedirect 를 반환한다.
- HttpResponseRedirect 는 한 개의 인자(사용자에게 재반응하여 보여주는 URL)만 취한다.
- POST 형식으로 전달한 뒤에 항상 HttpResponseRedirect 로 반환되어야한다. 장고라서가 아니라 웹 개발의 좋은 관행이다.
- reverse() 는 이 예제에서 HttpResponseRedirect 생성자에 대해 사용된 것이다.
- 이 함수는 view 함수에 대응한 URL이 hardcode 하는 것을 피하도록 해준다.
- 우리가 제어를 통과하고 URL pattern의 다양한 부분에 대한 뷰 함수의 이름을 고려한다.

**[polls/urls.py]**

```python
from django.conf.urls import url
from . import views # from polls import views


urlpatterns = [
...

  url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
]
```
<br><br>
#### \# results
**[polls/views.py]**
```python
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
```
**[polls/urls.py]**
```python
from django.conf.urls import url
from . import views # from polls import views

urlpatterns = [
...
  url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
]
```
**[polls/results.html]**
