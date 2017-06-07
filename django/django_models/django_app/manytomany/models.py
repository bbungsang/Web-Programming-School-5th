from django.db import models


class Lecture(models.Model):
    title = models.CharField(max_length=40)
    student = models.ManyToManyField('Student')

    def __str__(self):
        return '{}'.format(
            self.title,
        )
class Student(models.Model):
    name = models.CharField(max_length=20)
    # lecture = models.ForeignKey('Lecture')

    def __str__(self):
        return '{} / {}'.format(
            self.name,
            self.lecture,
        )


### extra fields on many-to-many relationships ###
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)