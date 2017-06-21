from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(
        User,
        max_length=30,
    )
    photo = models.ImageField(blank=True)
    comment = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modify_dated = models.DateTimeField(auto_now=True)