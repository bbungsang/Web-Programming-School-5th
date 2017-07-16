## URL
- `www.naver.com` (포스트 네임으로 특정 한대 이상의 서버를 가리킴) \+ 폴더 파일 구조와 비슷한 URL 리소스
- ?... `GET 인자` : 단순한 파라미터로 신경쓰지 않아도 된다.
- 주소 요청 시, 관련 작업을 함수(function)로서 구현하여 호출. 이러한 함수 정의는 `blog/views.py`에 한다.  
- 즉, 브라우저에서 주소를 요청하면 값을 전달하여 해당하는 함수를 호출하는 역할은 *URL* 이 하고, 그 값에 대한 응답을 *VIEW* 에서 하는 것이다.

[blog/urls.py]
```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    # name='post_list' 는 URL에 이름을 붙인 것으로 뷰를 식별한다.
]
```

[mysite/urls.py]
```python
url(r'^admin/', admin.site.urls),
# 장고가 admin/ 로 시작하는 모든 URL을 VIEW와 대조하여 찾아낸다. URL은 무수히 많으므로 정규표현식을 사용한다.

url(r'blog/', include('blog.urls')),
# http://127.0.0.1:8000/ 로 들어오는 모든 접속 요청을 blog.urls 로 전송
# blog.urls 에 정의되어 있는 부분을 mysite.urls에서도 사용할 수 있도록 가져오는 역할 : include
# blog/urls.py 에서 blog/... 주소를 사용할 때, 일일이 'blog/' 부분을 기입해야하는데, mysite/urls.py 에서 선언하면 그러한 수고를 덜 수 있다.
# 또한 blog/ 뒤에 $를 붙이지 않도록 주의한다. blog/urls.py 에서 특정 view 함수를 연결할 때에만 붙여준다.
```
<br>
 > `^post/(]d+)/$`

**^post/** : url이 `post/` 로 *시작* <br>
**(\\d+)** : `숫자`가 한 개 이상 <br>
**/$** : url 마지막이 `/` 로 *끝남*

## 뷰(view)
- 어플리케이션의 '로직'을 넣는 곳. url과 연결되어있는 함수기반, 클래스기반. <br>

###### 렌더
장고에서 지원해주는 템플릿 기반 시스템, 복잡한 문자열을 보다 쉽게 작업할 수 있도록 도와줌

[blog/view.py]
```python
from django.http import HttpResponse
from django.shortcuts import render

def post_list(request):
  return render(request, 'blog/post_list.html') # Template Loader
```

하지만 아직 `blog/template/blog/post_list.html` 을 아직 안 만들었기 때문에 템플릿 오류 발생
