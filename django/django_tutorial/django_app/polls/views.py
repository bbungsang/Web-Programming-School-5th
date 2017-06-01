from django.http import Http404

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 발행일 기준으로 순서대로 정렬되어 있는 Question 테이블의 리스트를 5개 발췌
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    # render()은 첫번째 인자로서 request 객체를 취한다. 두번째 인자는 template 의 이름, 세번째 인자는 딕셔너리이다.
    # context와 함께 걸러진 template의  HttpResponse 객체를 반환한다.


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
