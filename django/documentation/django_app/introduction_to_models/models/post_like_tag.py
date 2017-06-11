from django.db import models
from utils.models.mixins import TimeStampedMixin

class User(TimeStampedMixin):
    name = models.CharField(max_length=50)

class Post(TimeStampedMixin):
    author = models.ForeignKey(User)
    title = models.CharField(
        max_length=100,
        verbose_name='제목',
        help_text='포스팅 제목을 입력해주세요. 최대 100자 내외',
    )
    content = models.TextField(verbose_name='내용')  # 길이 제한이 없는 문자열
    tags = models.CharField(max_length=100, blank=True)

    like_users = models.ManyToManyField(User, related_name='posts_by_like_user')

class Comment(TimeStampedMixin):
    post = models.ForeignKey(Post)
    # 외래키로 필드를 생성하면 기입한 필드명이 아닌 '필드명_id' 의 이름으로 컬럼이 생성된다.
    author = models.ForeignKey(User)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PostLike(TimeStampedMixin):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    Created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{author}의 Post({post_content})에 대한 {like_user}의 좋아요 ({like_datetime})'.format(
            author=self.post.author.name,
            post_title=self.post.title,
            like_user=self.user.name,
            like_datetime=self.created_date,
        )

class Tag(TimeStampedMixin):
    pass