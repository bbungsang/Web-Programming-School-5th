## Django란?
- 파이썬으로 만들어진 웹어플리케이션 프레임워크로 가장 널리 쓰여진다. 최신버전 10.1.6 국내에서는 그 외 플라스크가 유명하다.<br><br>

## 웹 프레임워크가 왜 필요한가?
- 중복되는 코드가 분명히 존재(데이터베이스 접근, 템플릿 통해서 렌더링하는 등), 하지만 공통된 코드를 프레임워크로 정리해두면 좀 더 빠르고 안정적으로 개선할 수 있다.<br><br>

## 장고 기본 구조
```
[ 웹브라우저 ]
<--> URLCONF 미리 URL 별로 호출할 함수를 등록
<--> [ 뷰(View) ] URL에 맞춰 호출된 함수 <--> [ 템플릿(Template) ] HTML응답을 효과적으로 주기위한 HTML 응답 소스
<--> [ 모델(Model) ] SQL이 아닌 장고에서 지원해주는 ORM인 모델로써 데이터베이스 처리
<--> [ DB ]
```

## URL 설계

작업|URL|표현|연결
-|-|-|-
\#01|/blog/posts/ : 글목록|blog/views.py => post_list 함수로 표현|`url(r'^blog/posts/$', views.post_list)`
\#02|/blog/posts/new : 새 글 쓰기 폼|blog/views.py => post_new 함수로 표현|`url(r'^blog/posts/new/$', views.post_new)`
\#03|/blog/posts/10 : 10번 글 노출|blog/views.py => post_detail 함수로 표현|`url(r'^blog/posts/10', views.post_detail)`
\#04|/blog/posts/10/comments/new : 10번 글에 댓글쓰기 폼|comments_new 함수로 표현|`url(r'^blog/posts/10/comments/new', views.comments_new)`
\#05|/blog/posts/10/comments.json : 10번 글 댓글을 json형식으로 응답||
