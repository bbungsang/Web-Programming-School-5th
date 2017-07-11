# django 내부 라이브러리
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login
from django.contrib.auth.views import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers

# 설정한 것
from django.conf import settings
from member.forms import LoginForm, SignupForm, get_user_model

User = get_user_model()


def profile(request):
    return render(request, 'member/profile.html')


def login(request):

    # if request.method == 'POST':
    #     form = LoginForm(data=request.POST)
    #     print(form.is_valid())
    #     if form.is_valid():
    #         user = form.cleaned_data.get('user')
    #         django_login(request, user)
    #
    #         return redirect('post:post_list')
    #
    # else:
    #     if request.user.is_authenticated:
    #         return redirect('post:post_list')
    #     form = LoginForm()
    # context = {
    #     'form': form,
    # }
    #
    # return render(request, 'member/login.html', context)

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request', None)
    #     super(LoginForm, self).__init__(*args, **kwargs)

    providers = []

    # get_providers() 를 통해 settings/INSTALLED_APPS 내에서 활성화된 provider 목록을 얻어온다.
    for provider in get_providers():
        try:
            # provider 별 Client id/secret 이 등록되어 있는가? 를 확인하고, provider.social_app 에 할당
            # social_app 은 실제 provider 에는 없는 속성이다. 템플릿 내에서 참조하기 위해서 임의로 지정한 것
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)

        except SocialApp.DoesNotExist:
            provider.social_app = None

        providers.append(provider)
        print(providers)

    return auth_login(request,
                      authentication_form=LoginForm,
                      template_name='member/login.html',

                      # extra_context 를 통해서 추가 필요한 context 를 넘긴다.
                      extra_context={'providers': providers})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.create_user()
            print('회원가입을 축하합니다! 로그인해주세요.')
            return redirect('member:login')
    else:
        form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, 'member/signup.html', context)
