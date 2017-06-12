# import re
# from django.forms import ValidationError
from django.db import models
from django.contrib.auth.models import User


# def lnglat_validator(value):
#     if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
#         raise ValidationError('Invalid LngLat Type')

# class User(models.Model):
#     name = models.CharField(max_length=20)


class Post(models.Model):
    author = models.ForeignKey(User)  # 임포트한 User 사용
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 최초 저장될 때 최초 저장 일시
    modified_at = models.DateTimeField(auto_now=True)  # 갱신 시 저장 일시

    like_users = models.ManyToManyField(
        User,
        related_name='like_posts',
        through='PostLike',
    )
    tags = models.ManyToManyField('Tag')

    def add_comment(self, user, content):
        return self.comment_set.create(author=user, content=content)

    def add_tag(self, tag_name):
        tag, tag_created = Tag.objects.get_or_create(
            name=tag_name,
        )  # get_or_create() : 뒤의 객체가 있으면 가져오고 없으면 만들어서 가져옴, 객체 생성 시 True 를 반환
        if not self.tags.filter(name=tag_name).exists():
            self.tags.add(tag)

    def __str__(self):
        hi = self.comment_set.all()
        for hello in hi:
            return '작성자 : {{ author }} \n 댓글 정보 : {{ comment_author }} : {{ comment_content }} \n 태그 정보 : {{ tag_info }}'.format(
                author=self.author,
                comment_author=hello.author,
                comment_content=hello.content,
                tag_info=self.tag_set().name,
            )

    @property
    def like_count(self):
        return self.like_users.count()

    class Meta:
        ordering = ['-id']


class Comment(models.Model):
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    # 외래키로 필드를 생성하면 기입한 필드명이 아닌 '필드명_id' 의 이름으로 컬럼이 생성된다.
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    like_users = models.ManyToManyField(
        User,
        through='CommentsLike',
        related_name='like_comments',
    )


class CommentsLike(models.Model):
    comment = models.ForeignKey(Comment)
    user = models.ForeignKey(User)
    created_date = models.DateField(auto_now_add=True)


class PostLike(models.Model):
    # LIKE = 1
    # DISLIKE = -1
    #
    # VOTES = (
    #     (LIKE, 'Like')
    #     (DISLIKE, 'Dislike')
    # )
    #
    # vote = models.SmallIntegerField(verbose_name=())
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'post_post_like_users'


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Tag({})'.format(self.name)
