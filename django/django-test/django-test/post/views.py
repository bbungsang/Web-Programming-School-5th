from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect

from post.forms import PostForm
from post.models import Post

User = get_user_model()


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            # comment = form.cleaned_data['comment']
            # Post.objects.create(
            #     author=request.user,
            #     comment=comment,
            # )
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post:post_list')
    else:
        # else 는 폼에 대한 에러를 검출하기 위해 사용
        # 검증을 위해서 폼을 사용
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'post/post_create.html', context)