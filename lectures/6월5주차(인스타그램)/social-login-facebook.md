> 웹에서 소셜 로그인을 하는 방법은 2가지가 있다. ٩(๑\`^´๑)۶
1. 앞 단에서 자바스크립트를 활용하여 로그인하기
2. 서버단에서 로그인 처리 <br>
\- **로그인 플로 직접 빌드** : 앱, 자바스크립트는 `SDK`를 사용하지만 그렇지 않다면, `로그인 flow를 직접 빌드하는 방식` 을 사용한다.

# OAuth란?
- 제각각인 인증방식을 `표준화`한 것이며, OAuth 를 공유하는 어플리케이션끼리는 OAuth 로 인해 별도의 인증 과정 없이 사용자 인증(로그인)이 가능하다.
- 페이스북이 이미 브라우저에 로그인되어 있는 경우(서버 측에 페이스북 아이디와 비밀번호 정보를 가지고 있을 경우), 자동으로 유저 정보를 가져와 로그인이 된다.
- 하지만 그렇지 않다면, 페이스북에 로그인을 시켜줘야한다.
- 즉, *페이스북으로부터 유저 정보를 받아와야 페이스북 로그인이 가능* 해진다.

### OAuth 의 인증방식 순서
> 그 전에 OAuth 용어에 대해 간략히 알고가자<br>
- **User** : Consumer가 서비스하는 어플리케이션의 이용자 (장고 어플리케이션 사용자)
- **Consumer** : User 의 요청을 받고 응답하며, Open API 를 이용하여 Service Provider 에게 접근하는 웹사이트 또는 어플리케이션 (장고 어플리케이션)
- **Service Provider** : Open API 를 제공하는 서비스 (페이스북)
- **Request Token** : Consmer 가 User 의 Service Provider 으로의 접근 권한을 인증받기 위한 정보가 담겨있으며, 후에 Access Token 으로 변환된다.
- **Access Token** : 인증 후, Cunsumer 가 필요로하는 User 의 보호된 정보에 접근하기 위한 키를 포함한 값이다.

1. Consumer 가 Service Provider 에게 Request Token 을 요청한다.
2. Service Provider 가 Consumer 에게 Request Token 을 발급해준다.
3. Consumer 가 User 를 Service Provider 로 이동시키고, 여기에서 사용자 인증이 수행된다.
4. 인증 완료 후, User 는 다시 Consumer 로 이동한다.
5. Consumer 가 필요한 정보를 Service Provider 로 부터 받기 위해 Access Token 을 요청한다.
6. Service Provider 에게 발급받은 Access Token 을 이용하여 User 정보에 접근한다.

# 페이스북으로 로그인하기
#### 페이스북 개발자 페이지에서 앱 ID 와 시크릿 코드를 얻자 [Click!](developers.facebook.com/docs/facebook-login)
1. 우리 서비스에 대해서 특별히 앱을 하나 생성한다.
2. [새 앱 추가]에서 앱 이름과 이메일 주소를 기입한다.
3. 대시보드에서 앱 ID 와 시크릿 코드를 확인한다. *시크릿 코드는 비밀번호 입력 후 접근이 가능하며 노출되면 안된다.*

#### 뷰를 작성하기에 앞서 settings 에 추가해야할 항목을 먼저 살펴보자
- 시크릿 코드와 같이 노출되면 안돼는 정보가 있을 경우, 프로젝트 폴더에서 해당 코드를 작성할 디렉토리를 생성한다.
- 그 아래 페이스북 시크릿 코드를 작성할 json 파일을 만든 후, .gitignore 항목에 추가시킨다.

> 페이스북 가이드 ʕ•̀ω•́ʔ✧
- 악의적인 용도로 구성된 데이터를 사용할 수 있기 때문에 액세스 토큰을 생성하기 전에 앱 사용자가 응답 데이터가 있는 사용자인지 확인해야 합니다.
- `code` 가 수신되면 엔드포인트를 사용하여 액세스 토큰과 교환해야 합니다. 이 호출에서는 앱 시크릿 코드가 사용되므로 서버 간에 이루어져야 합니다. (앱 시크릿 코드는 클라이언트 코드에 있지 않아야 합니다.)

[프로젝트 구조]
```txt
project_folder/
    .config_secret/
        api_secret_keys.json
    django_app/
        config/
        post/
        member/
        manage.py
        [...]
```

[.config_secret/api_secret_keys.json]
```python
{
  "facebook": {
    "secret_key": "xxxxx(발급 받은 페이스북 시크릿 키)"
  }
}
```

[django_app/config/settings.py]
- settings 에서 .config_secret 파일의 경로를 설정한 후, 위 내용을 변수에 할당한다.

```python
# root directory 설정
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# BASE_DIR 인 django_app 에서 상위 폴더인 프로젝트 폴더 경로를 ROOT_DIR 에 할당한다.
ROOT_DIR = os.path.dirname(BASE_DIR)

# Facebook
FACEBOOK_APP_ID = '448444942187343'

# 프로젝트 폴더 하위 폴더인 .config_secret 의 경로를 CONFIG_SECRET_DIR 에 할당한다.
CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, '.config_secret')

# .config_secret 의 파일인 api_secret_keys.json 의 경로를 API_SECRET_KEYS 에 할당한다.
API_SECRET_KEYS = os.path.join(CONFIG_SECRET_DIR, 'api_secret_keys.json')

# api_secret_keys.json 파일을 열고 해당 내용을 api_secret_keys 에 할당한다.
api_secret_keys = json.loads(open(API_SECRET_KEYS).read())

# api_secret_keys 의 facebook 항목 내의 secret_key 의 value 를 FACEBOOK_SECRET_CODE 에 할당한다.
FACEBOOK_SECRET_CODE = api_secret_keys['facebook']['secret_key']

[...]
```

#### 뷰로 넘어가는 단계
- 뷰가 일을 처리하기 위해서는 템플릿에 뷰에게 일을 시킬 수 있는 장치를 마련해야한다.
- a 태그에 뷰로 넘어가는 url 을 설정해보자.
- href 속성에 {% raw %}`https://www.facebook.com/v2.9/dialog/oauth?
  client_id={app-id}
  &redirect_uri={redirect-uri}{%url '<app-name>:<view-name>'%}`{% endraw %} 와 같은 url 을 통해 code 데이터를 얻고, 해당 code 를 뷰에서 처리하도록 지시하였다.
- **app-id** 는 페이스북으로부터 발급받은 FACEBOOK_APP_ID 를 의미한다.
- **redirect_uri** 는 페이스북 로그인 대화상자로 부터 얻은 정보를 처리할 뷰를 호출하는 url 을 의미한다.
- `The redircet_uri URL must be absolute` 반드시 `http` 로 시작하는 완벽한 주소여야한다. 상대 url 이 아닌 `절대 url` (http://localhost:8080/member/login/kakao 의 형태)

[templates/member/login.html]
```html
{% raw %}
<a href="https://www.facebook.com/v2.9/dialog/oauth?
  client_id='xxxxxyyyyy'
  &redirect_uri='http://localhost:8080/member/login/kakao'{% url 'member:kakao_login' %}"></a>
{% endraw %}
```
- 길고 어려운 주소이므로 context_processor 를 거쳐 정보를 호출하는 방식을 이용하자 [Context Processor]()

#### facebook_login 뷰 만들기
[views/auth.py]
```python
def facebook_login(request):

    # 페이스북 로그인 버튼의 URL 을 통하여 facebook_login view 가 처음 호출될 때, 'code' request GET parameter 받으며, 'code' 가 없으면 오류 발생한다.
    code = request.GET.get('code')

    ##%%&& 액세스 토큰 얻기 &&%%##

    """
    GET https://graph.facebook.com/v2.9/oauth/access_token?
       client_id={app-id}
       &redirect_uri={redirect-uri}
       &client_secret={app-secret}
       &code={code-parameter}  
    """

    # code 인자를 받아서 Access Token 교환을 URL 에 요청후, 해당 Access Token 을 받는다.
    def get_access_token(code):

        # Access Token 을 교환할 URL
        exchange_access_token_url = 'https://graph.facebook.com/v2.9/oauth/access_token'

        # 이전에 요청했던 URL 과 같은 값 생성(Access Token 요청시 필요)
        redirect_uri = '{}{}'.format(
            settings.SITE_URL,
            request.path,
        )

        # Access Token 요청시 필요한 파라미터
        exchange_access_token_url_params = {
            'client_id': settings.FACEBOOK_APP_ID,
            'redirect_uri': redirect_uri,
            'client_secret': settings.FACEBOOK_SECRET_CODE,
            'code': code,
        }

        # Access Token 을 요청한다.
        response = requests.get(
            exchange_access_token_url,
            params=exchange_access_token_url_params,
        )
        result = response.json()

        """
        성공하면 다음과 같다.
        {
          "access_token": {access-token},
          "token_type": {type},
          "expires_in":  {seconds-til-expiration}
        }
        """

        # 응답받은 결과값에 'access_token'이라는 key 가 존재하면,
        if 'access_token' in result:
            # access_token key 의 value 를 반환한다.
            return result['access_token']
        elif 'error' in result:
            raise Exception(result)
        else:
            raise Exception('Unknown error')

    ##%%&& 액세스 토큰이 올바른지 검사 &&%%##
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

    ##%%&& 에러 메세지를 request 에 추가, 이전 페이지로 redirect &&%%##
    def add_message_and_redirect_referer():
        error_message = 'Facebook login error'
        messages.error(request, error_message)

        # 이전 URL 로 리다이렉트
        return redirect(request.META['HTTP_REFERER'])

    ##%%&& 발급받은 Access Token 을 이용하여 User 정보에 접근 &&%%##
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

    ##%%&& 페이스북 로그인을 위해 정의한 함수 실행하기 &&%%##
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
    # 이 예외는 utils/exceptions.py 에 정의되어 있다. 
    except GetAccessTokenException as e:
        print(e.code)
        print(e.message)
        return add_message_and_redirect_referer()
    except DebugTokenException as e:
        print(e.code)
        print(e.message)
        return add_message_and_redirect_referer()
```
