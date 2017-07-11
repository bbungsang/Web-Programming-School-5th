from django.shortcuts import get_object_or_404, redirect

from post.models import Post
from post.forms.comment import CommentForm


def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
        return redirect('post:post_detail', post_pk=post.pk)