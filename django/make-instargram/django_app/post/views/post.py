from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from post.forms.post import PostForm
from post.forms import CommentForm
from post.models import Post, Tag


def post_list_original(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'comment_form': CommentForm(),
    }
    return render(request, 'post/post_list.html', context)


def post_list(request):
    all_posts = Post.objects.all()
    p = Paginator(all_posts, 3)
    page_num = request.GET.get('page')

    try:
        posts = p.page(page_num)

    except PageNotAnInteger:
        posts = p.page(1)
    except EmptyPage:
        posts = p.page(p.num_pages)

    context = {
        'posts': posts,
        'comment_form': CommentForm(auto_id=False),
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    context = {
        'post': post,
    }
    return render(request, 'post/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():

            # post = form.save(commit=False)
            # post.author = request.user
            # post.save()

            post = form.save(author=request.user)
            post.save()

            return redirect('post:post_detail', post_pk=post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'post/post_create.html', context)


def post_modify(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post:post_detail', post_pk=post.pk)
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
    }
    return render(request, 'post/post_create.html', context)


def post_delete(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_pk)
        post.delete()
        return redirect('post:post_list')
    return render(request, 'post/post_delete.html')


def post_like_toggle(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    post_like, post_like_created = post.postlike_set.get_or_create(
        user=request.user,
    )

    if not post_like_created:
        post_like.delete()

    return redirect('post:post_detail', post_pk=post.pk)


def hashtag_post_list(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)

    posts = Post.objects.filter(my_comment__tags=tag)
    posts_count = posts.count()

    context = {
        'tag': tag,
        'posts': posts,
        'posts_count': posts_count,
    }
    return render(request, 'post/hashtag_post_list.html', context)


