from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    # lecture = models.ManyToManyField(
    #     'Lecture',
    # )

    def __str__(self):
        return self.name

    @property
    def find_room(self):
        e_list = []
        for lecture in self.lecture_set.all():
            e_list.append(lecture.room.room)
        return e_list


class Lecture(models.Model):
    title = models.CharField(max_length=40)
    student = models.ManyToManyField(
        'Student',
        through='Enrollment'
    )
    room = models.OneToOneField(
        'Classroom',
    )

    def __str__(self):
        return '{}/{}'.format(
            self.title,
            self.room,
        )


class Enrollment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )
    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.CASCADE,
    )
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{student}님의 {lecture} 등록일은 {date_joined} 입니다.'.format(
            student=self.student,
            lecture=self.lecture,
            date_joined=self.date_joined,
        )

class Classroom(models.Model):
    room = models.CharField(max_length=1)

    def __str__(self):
        return self.room


# many to many 빼고 다 넣을 것!

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