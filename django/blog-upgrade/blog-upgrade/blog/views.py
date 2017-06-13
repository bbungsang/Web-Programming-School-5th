from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader

from .models import Post
from .form import PostForm

def post_list(request):
    posts = Post.objects.all()
    context = {
        'post_list': posts,
    }
    return render(
        request,
        'blog/post_list.html',
        context=context,
    ) # 반드시 앱 이름을 쓰고 그 뒤에 파일명 쓰기


def post_detail(request, pk):

    # 모델(데이터베이스)에서 post_pk에 해당하는 Post 객체를 가져와 post 변수에 할당
    # get() 결과가 1개일 때만, 따라서 단 한 개의 Post 객체를 가져와야 하므로 get()을 사용

    # 가져오는 과정에서 예외처리를 한다 (Model.DoesNotExist)
    try:
        post = get_object_or_404(Post, pk=pk)
    except Post.DoesNotExist as e:
        # 1. 404 Not found 를 띄어줌
        return HttpResponseNotFound('Post not found, detail: {}'.format(e))

        # 2. redirect() 사용
        # post_list view 로 돌아감
        # return redirect('post:post_list')

    # request에 대해 response를 돌려줄 때는 HttpResponse나 render를 사용
    # template를 사용하려면 render()를 사용한다.
    # render()는 장고가 템플릿을 검색할 수 있는 모든 디렉토리를 순회하며 인자로 저어진 문자열값과 일치하는 템플릿 여부를 확인 후,
    # 결과를 리턴 (django.template.backends.django.Template
    # 축약버전과 그렇지 않은 버전이 있다.
    # 축약버전이 아닐 경우, (전체 과정(loader, HttpResponse)을 기술
    template = loader.get_template('blog/post_detail.html')

    # dict형 변수 context의 'post'키에 post(Post객체)를 할당
    context = {
        'post': post,
    }

    # template에 인자로 주어진 context, request를 render함수를 사용해서 해당 템플릿을 string으로 변환
    rendered_string = template.render(context=context, request=request)

    # 변환된 string을 HttpResponse() 인자로 돌려준다.
    return HttpResponse(rendered_string)

    # HttpResponse(string)
    # redirect(어디로 갈지에 대한 url)


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
            # 이 처럼 뷰 이름과 인자를 넘겨주면 알아서 reverse() 실행
    else:
        form = PostForm()

    return render(request, 'blog/post_create.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

def post_delete(request, pk):
    item = Post.objects.get(id=pk)
    item.delete()
    return redirect('post_list',)

def comment_list():
    pass

def comment_edit():
    pass

def comment_delete():
    pass
