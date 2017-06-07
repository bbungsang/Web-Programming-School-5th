from django.db import models

class CommonInfo(models.Model_):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    def __str__(self):
        return 'HomeGroup {}\'s student({}, {})'.format(
            self.calss_,
            self.name,
            self.age
        )

    class Meta:
        db_table = 'introduction_to_models_abc_student'

class Teacher(CommonInfo):
    class_ = models.CharField(max_length=20)

    def __str__(self):
        return 'Class {} \'s teeacher ({}, {})'.format(
            self.class_,
            self.name,
            self,age
        )

    class Meta:
        db_table = 'introduction_to_models.abc_teacher'