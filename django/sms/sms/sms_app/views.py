from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from sms_app.models import SmsInfo
from .forms import SmsForm

'''
def sms_send(request) 뷰 생성, POST 요청에 받는 사람 번호와 내용을 전송해서 SMS 전송 기능 GET 요청시에는 form 만 보여줌
Form 클래스 사용은 선택적
'''


def sms_send(request):
    if request.method == 'POST':
        form = SmsForm(data=request.POST)
        if form.is_valid():
            form.check_info()
            sms = form.save()
            return redirect('sms_app:sms_result', sms_pk=sms.pk)
    else:
        form = SmsForm()
    context = {
        'form': form,
    }
    return render(request, 'sms_send.html', context)


def sms_result(request, sms_pk):
    sms = get_object_or_404(SmsInfo, pk=sms_pk)
    context = {
        'sms': sms,
    }
    return render(request, 'sms_result.html', context)