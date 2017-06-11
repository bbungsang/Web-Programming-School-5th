import re
from django.forms import ValidationError
from django.db import models

from django.contrib.contenttypes.models import contenttype
from django.contrib.contenttypes.fields import GenericForeignKey

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(
        max_length=100,
        verbose_name='제목',
        help_text='포스팅 제목을 입력해주세요. 최대 100자 내외',
    ) # 길이 제한이 있는 문자열
    content = models.TextField(verbose_name='내용') # 길이 제한이 없는 문자열
    tags = models.CharField(max_length=100, blank=True)
    acreated_at = models.DateTimeField(auto_now_add=True) # 최초 저장될 때 최초 저장 일시
    updated_at = models.DateTimeField(auto_now=True) # 갱신 시 저장 일시

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    # 외래키로 필드를 생성하면 기입한 필드명이 아닌 '필드명_id' 의 이름으로 컬럼이 생성된다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (LIKE, 'Like')
        (DISLIKE, 'Dislike')
    )

    vote = models.SmallIntegerField(verbose_name=())
