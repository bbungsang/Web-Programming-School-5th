from django.shortcuts import render
from django.http import HttpResponse

from .models import User


def login(request, name, pwd):
    if request.method == 'POST':
        user_info = User.objects.get(name=name)
        if pwd == user_info.pwd:
            context = {
                'username': name,
            }
            return render(
                request,
                'blog/post_list.html',
                context=context,
            )

        else:
            return HttpResponse("Login invalid!")
    else:
        return render(request, 'member/login.html')