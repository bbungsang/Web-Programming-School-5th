# from django.contrib.auth.models import User
from django.db import models

from django.conf import settings

# class User(models.Model):
#     name = models.CharField(max_length=20)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)  # 임포트한 User 사용
    photo = models.ImageField(upload_to='post/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 최초 저장될 때 최초 저장 일시
    modified_at = models.DateTimeField(auto_now=True)  # 갱신 시 저장 일시

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_posts',
        through='PostLike',
    )
    tags = models.ManyToManyField('Tag', blank=True)

    def add_comment(self, user, content):
        return self.comment_set.create(author=user, content=content)

    def add_tag(self, tag_name):
        tag, tag_created = Tag.objects.get_or_create(
            name=tag_name,
        )  # get_or_create() : 뒤의 객체가 있으면 가져오고 없으면 만들어서 가져옴, 객체 생성 시 True 를 반환
        if not self.tags.filter(name=tag_name).exists():
            self.tags.add(tag)

    @property
    def like_count(self):
        return self.like_users.count()

    class Meta:
        ordering = ['-id']


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    # 외래키로 필드를 생성하면 기입한 필드명이 아닌 '필드명_id' 의 이름으로 컬럼이 생성된다.
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='CommentsLike',
        related_name='like_comments',
    )


class CommentsLike(models.Model):
    comment = models.ForeignKey(Comment)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateField(auto_now_add=True)


class PostLike(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     db_table = 'post_post_like_users'


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Tag({})'.format(self.name)
