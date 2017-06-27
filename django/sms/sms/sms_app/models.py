from django.db import models


class SmsInfo(models.Model):
    to_num = models.CharField(max_length=11)
    from_num = models.CharField(max_length=11)
    content = models.TextField(blank=True)
