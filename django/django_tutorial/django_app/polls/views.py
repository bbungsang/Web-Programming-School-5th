from django.core.checks import messages
from django.shortcuts import get_object_or_404, render, redirect
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
    # context 와 함께 걸러진 template 의  HttpResponse 객체를 반환한다.


def detail(request, question_id):
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    """
    # 만약에 요청된 ID에 대한 question 이 존재하지 않으면 view 는 Http404 예외를 일으킨다.

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # 모델의 관리자인 get_object_or_404()의 인자는 만약 객자가 존재하지 않으면 Http404를 일으킨다.
    # 왜 DoesNotExist 예외처리를 안 하고 get_object_or_404()를 쓸까? 그 까닭은 장고 중요한 목표의 하나는 느슨한 결합을 유지하는 것이다.
    # 몇 몇의 제어된 결합은 django.shortcuts 모듈에서 도입된다.


def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    #     # requst.POST['choice'] 는 선택된 choice의 ID 값을 string 으로  반환한다. request.POST value는 항상 string 형이다.
    #     print('hello')
    # except (KeyError, Choice.DoesNotExist):
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # choice count 를 증가시킨 후에 코드는 HttpResponseRedirect 를 반환한다.
    #     # HttpResponseRedirect 는 한 개의 인자(사용자에게 재반응하여 보여주는 URL)만 취한다.
    #     # POST 형식으로 전달한 뒤에 항상 HttpResponseRedirect 로 반환되어야한다. 장고라서가 아니라 웹 개발의 좋은 관행이다.

    if request.method == 'POST':
        data = request.POST
        try:
            choice_id = data['choice']
            choice = Choice.objects.get(id=choice_id)
            choice.votes += 1
            choice.save()
            return redirect('polls:results', question_id)
        except (KeyError, Choice.DoesNotExist):
            messages.add_message(
                request,
                messages.ERROR,
                "You didn't select a choice"
            )

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # reverse() 는 이 예제에서 HttpResponseRedirect 생성자에 대해 사용된 것이다.
    # 이 함수는 view 함수에 대응한 URL이 hardcode 하는 것을 피하도록 해준다.
    # 우리가 제어를 통과하고 URL pattern의 다양한 부분에 대한 뷰 함수의 이름을 고려한다.



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

    # result의 method가 POST 방식일 때,
    # 전달받은 데이터 중 'choice' 키에 해당하는 값을
    # HttpResponse에 적절히 돌려준다

    # choice 키에 해당하는 Choice인스턴스의 vote값을 1 증가시키고
    # 데이터베이스에 변경 사항을 반영
    # 이후 results 페이지로 redirect
