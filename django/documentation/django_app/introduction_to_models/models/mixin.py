from django.db import models
from utils.models.mixins import TimeStampeMixin

class Post(TimeStampeMixin):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=128)
    content = models.TextField()

class Comment(TimeStampeMixin):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    content = models.TextField()

class User(TimeStampeMixin):
    name = models.ForeignKey(Post, on_delete=models.CASCADE)