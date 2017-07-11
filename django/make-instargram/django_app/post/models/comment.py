import re
from django.db import models
from django.urls import reverse

from config import settings
from .post import Post
from .others import Tag


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    content = models.TextField()
    tags = models.ManyToManyField('Tag')
    html_content = models.TextField(blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='CommentLike',
        related_name='like_comments',
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.make_html_content_add_tags()

    def make_html_content_add_tags(self, ):
        p = re.compile(r'(#\w+)')
        tag_name_list = re.findall(p, self.content)
        edit_content = self.content

        for tag_name in tag_name_list:
            tag, _ = Tag.objects.get_or_create(name=tag_name.replace('#', ''))

            change_tag = '<a href="{url}">{tag_name}</a>'.format(
                url=reverse('post:hashtag_post_list', kwargs={'tag_name': tag_name.replace('#', '')}),
                tag_name=tag_name,
            )

            edit_content = edit_content.replace(tag_name, change_tag)
            if not self.tags.filter(pk=tag.pk):
                self.tags.add(tag)

        self.html_content = edit_content
        super().save(update_fields=['html_content'])


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)