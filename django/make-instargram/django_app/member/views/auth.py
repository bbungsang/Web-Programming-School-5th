# django 내부 라이브러리
import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers

# 설정한 것
from django.conf import settings
from member.forms import LoginForm, SignupForm, get_user_model
from utils.exceptions import DebugTokenException, GetAccessTokenException

User = get_user_model()


def profile(request):
    return render(request, 'member/profile.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.cleaned_data.get('user')
            django_login(request, user)

            return redirect('post:post_list')

    else:
        if request.user.is_authenticated:
            return redirect('post:post_list')
        form = LoginForm()

    providers = []

    for provider in get_providers():
        try:
            # provider 별 Client id/secret 이 등록되어 있는가? 를 확인하고, provider.social_app 에 할당
            # social_app 은 실제 provider 에는 없는 속성이다. 템플릿 내에서 참조하기 위해서 임의로 지정한 것
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)

        except SocialApp.DoesNotExist:
            provider.social_app = None

        providers.append(provider)

    # return auth_login(request,
    #                   authentication_form=LoginForm,
    #                   template_name='member/allauth_login.html',
    #
    #                   # extra_context 를 통해서 추가 필요한 context 를 넘긴다.
    #                   extra_context={'providers': providers})

    context = {
        'form': form,
        'providers': providers,
    }
    return render(request, 'member/login.html', context)


def facebook_login(request):

    # 페이스북 로그인 버튼의 URL 을 통하여 facebook_login view 가 처음 호출될 때, 'code' request GET parameter 받으며, 'code' 가 없으면 오류 발생한다.
    code = request.GET.get('code')

    ########################
    #### 액세스 토큰 얻기 ####
    # code 인자를 받아서 Access Token 교환을 URL 에 요청후, 해당 Access Token 을 받는다.
    def get_access_token(code):

        # Access Token 을 교환할 URL
        exchange_access_token_url = 'https://graph.facebook.com/v2.9/oauth/access_token'

        # 이전에 요청했던 URL 과 같은 값 생성(Access Token 요청시 필요)
        redirect_uri = '{}{}'.format(
            settings.SITE_URL,
            request.path,
        )

        # # Access Token 을 교환할 URL
        # exchange_access_token_url = 'https://graph.facebook.com/v2.9/oauth/access_token'

        # Access Token 요청시 필요한 파라미터
        exchange_access_token_url_params = {
            'client_id': settings.FACEBOOK_APP_ID,
            'redirect_uri': redirect_uri,
            'client_secret': settings.FACEBOOK_SECRET_CODE,
            'code': code,
        }
        print(exchange_access_token_url_params)

        # Access Token 을 요청한다.
        response = requests.get(
            exchange_access_token_url,
            params=exchange_access_token_url_params,
        )
        result = response.json()
        print(result)

        # 응답받은 결과값에 'access_token'이라는 key 가 존재하면,
        if 'access_token' in result:
            # access_token key 의 value 를 반환한다.
            return result['access_token']
        elif 'error' in result:
            raise Exception(result)
        else:
            raise Exception('Unknown error')

    ##################################
    #### 액세스 토큰이 올바른지 검사 ####
    def debug_token(token):
        app_access_token = '{}|{}'.format(
            settings.FACEBOOK_APP_ID,
            settings.FACEBOOK_SECRET_CODE,
        )

        debug_token_url = 'https://graph.facebook.com/debug_token'
        debug_token_url_params = {
            'input_token': token,
            'access_token': app_access_token
        }

        response = requests.get(debug_token_url, debug_token_url_params)
        result = response.json()

        if 'error' in result['data']:
            raise DebugTokenException(result)
        else:
            return result

    ###########################################################
    #### 에러 메세지를 request 에 추가, 이전 페이지로 redirect ####
    def add_message_and_redirect_referer():
        error_message = 'Facebook login error'
        messages.error(request, error_message)

        # 이전 URL 로 리다이렉트
        return redirect(request.META['HTTP_REFERER'])

    ########################################################
    #### 발급받은 Access Token 을 이용하여 User 정보에 접근 ####
    def get_user_info(user_id, token):
        url_user_info = 'https://graph.facebook.com/v2.9/{user_id}'.format(user_id=user_id)
        url_user_info_params = {
            'access_token': token,
            'fields': ','.join([
                'id',
                'name',
                'email',
            ])
        }
        response = requests.get(url_user_info, params=url_user_info_params)
        result = response.json()
        return result

    ################################################
    #### 페이스북 로그인을 위해 정의한 함수 실행하기 ####

    # code 가 없으면 에러 메세지를 request 에 추가하고 이전 페이지로 redirect
    if not code:
        return add_message_and_redirect_referer()

    try:
        access_token = get_access_token(code)
        debug_result = debug_token(access_token)
        user_info = get_user_info(user_id=debug_result['data']['user_id'], token=access_token)
        user = User.objects.get_or_create_facebook_user(user_info)

        django_login(request, user)
        return redirect('post:post_list')
    except GetAccessTokenException as e:
        print(e.code)
        print(e.message)
        return add_message_and_redirect_referer()
    except DebugTokenException as e:
        print(e.code)
        print(e.message)
        return add_message_and_redirect_referer()


def kakao_login(request):

    code = request.GET.get('code')

    ########################
    #### 액세스 토큰 얻기 ####
    # code 인자를 받아서 Access Token 교환을 URL 에 요청후, 해당 Access Token 을 받는다.
    def get_access_token(code):

        # Access Token 을 교환할 URL
        exchange_access_token_url = 'https://kauth.kakao.com/oauth/token'

        # 이전에 요청했던 URL 과 같은 값 생성(Access Token 요청시 필요)
        redirect_uri = settings.KAKAO_REDIRECT_URI

        # Access Token 요청시 필요한 파라미터
        exchange_access_token_url_params = {
            'grant_type': 'authorization_code',
            'client_id': settings.KAKAO_APP_ID,
            'redirect_uri': redirect_uri,
            'code': code,
            'client_secret': settings.KAKAO_CLIENT_SECRET,
        }

        # Access Token 을 요청한다.
        response = requests.get(
            exchange_access_token_url,
            params=exchange_access_token_url_params,
        )
        result = response.json()
        print("get_access_token result :", result)

        # 응답받은 결과값에 'access_token'이라는 key 가 존재하면,
        if 'access_token' in result:
            # access_token key 의 value 를 반환한다.
            return result['access_token']
        elif 'error' in result:
            raise Exception(result)
        else:
            raise Exception('Unknown error')

    def add_message_and_redirect_referer():
        error_message = 'Kakao login error'
        messages.error(request, error_message)

        # 이전 URL 로 리다이렉트
        return redirect(request.META['HTTP_REFERER'])

    def app_connection(access_token):
        url = 'https://kapi.kakao.com/v1/user/signup'
        access_token = "Bearer " + access_token
        response = requests.get(
            url,
            headers={
                "Authorization": access_token,
                # "Content-Type": "Content-Type: application/x-www-form-urlencoded;charset=utf-8",
                     },
        )
        print(response)
        result = response.json()
        print('app_connection result :', result)
        return result


    ########################################################
    #### 발급받은 Access Token 을 이용하여 User 정보에 접근 ####
    def get_user_info(app_connection):
        url = 'https://kapi.kakao.com/v1/user/me'
        # url_user_info_params = {
        #     'target_id_type': 'user_id',
        #     'target_id': app_connection,
        #     'propertyKeys': [
        #         'name',
        #     ]
        # }
        response = requests.get(
            url,
            headers={
                "Authorization": "Bearer " + access_token,
                # "Content-Type": "Content-Type: application/x-www-form-urlencoded;charset=utf-8",
            },
        )
        result = response.json()
        print('get_user_info result :', result)
        # 요청이 성공하면 응답 바디에 JSON 객체로 id, kaccount_email 을 포함한다.
        return result

    ################################################
    #### 카카오 로그인을 위해 정의한 함수 실행하기 ####

    # code 가 없으면 에러 메세지를 request 에 추가하고 이전 페이지로 redirect
    if not code:
        return add_message_and_redirect_referer()

    try:
        access_token = get_access_token(code)
        # debug_result = debug_token(access_token)
        app_connection = app_connection(access_token)
        user_info = get_user_info(app_connection)
        user = User.objects.get_or_create_kakao_user(user_info)

        django_login(request, user)
        return redirect('post:post_list')
    except GetAccessTokenException as e:
        print(e.code)
        print(e.message)
        return add_message_and_redirect_referer()
    except DebugTokenException as e:
        print(e.code)
        print(e.message)
        return add_message_and_redirect_referer()


def signup(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            # form.create_user()
            form.save()
            print('회원가입을 축하합니다! 로그인해주세요.')
            return redirect('member:login')
    else:
        form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, 'member/signup.html', context)
