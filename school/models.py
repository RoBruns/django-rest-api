from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVELS = (
        ('B', 'Basic'),
        ('I', 'Intermediat'),
        ('A', 'Advanced'),
    )

    course_code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(
        max_length=1,
        choices=LEVELS,
        blank=False,
        null=False,
        default='B')

    def __str__(self):
        return self.description


class Registration(models.Model):
    PERIODS = (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('N', 'Night'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now=True)
    period = models.CharField(
        max_length=1,
        choices=PERIODS,
        blank=False,
        null=False,
        default='M')
