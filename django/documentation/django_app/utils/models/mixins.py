from django.db import models

class TimeStampeMixin(models.Model):
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    class Meta:
        abstract = True