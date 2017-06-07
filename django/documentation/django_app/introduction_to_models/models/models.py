from django.db import models

# class Person(models.Model):
#     SHIRT_SIZES = (
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#
#     )
#
#     PERSON_TYPES = (
#         ('student', '학생'),
#         ('teacher', '선생'),
#     )
#
#     persontype = models.CharField(
#         '유형',
#         max_length=10,
#         choices=PERSON_TYPES,
#         default=PERSON_TYPES[0][0],
#     )
#     # teacher 속성 지정 (ForeignKey, 'self'를 이용해 자기 자신을 가리킬, null=Ture 허용)
#     teacher = models.ForeignKey('self',
#                                 null=True,
#                                 blank=True,
#                                 on_delete=models.CASCADE
#                                 )
#     name = models.CharField(max_length=60)
#     shirt_size = models.CharField(
#         '셔츠사이즈',
#         max_length=1,
#         choices=SHIRT_SIZES,
#         help_text="약간 작게 나왔으니 참고해주세요."
#     )


class Fruit(models.Model):
  name = models.CharField(max_length=100, primary_key=True)


class Poll(models.Model):
    pass

class Site(models.Model):
    pass

class Place(models.Model):
    pass

poll = models.ForeignKey(
    Poll,
    on_delete=models.CASCADE,
    verbose_name="the related poll",
)
sites = models.ManyToManyField(Site, verbose_name="list of sites")
place = models.OneToOneField(
    Place,
    on_delete=models.CASCADE,
    verbose_name="related place",
)

class Topping(models.Model):
    pass

class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)

### Many-to-one relationships ###
class Manufacturer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=40)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

### Extra fields on many-to-many relationships ###
##################################################
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

# intermediary model
class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_join = models.DateField()
    invite_reason = models.CharField(max_length=64)