import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField('질문', max_length=200)
    pub_date = models.DateTimeField('발행일')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

    """
    >>> from polls.models import *
    >>> Question.objects.all()
    <QuerySet [<Question: What's up?>]>
    """
    # 안 했을 시, <QuerySet []> 으로 표현된다.

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently'



class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        verbose_name='해당 질문',
        on_delete=models.CASCADE
    )
    choice_text = models.CharField('선택 내용', max_length=200)
    votes = models.IntegerField('총 투표수', default=0)

    def __str__(self):
        return self.choice_text


