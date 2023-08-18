from django.db import models


class Courses(models.Model):

    name = models.CharField(max_length=50, unique=True, verbose_name='Имя пользователя дерева', null=True, blank=True)
    start_date = models.DateTimeField()


class Student(models.Model):

    name = models.CharField(max_length=50, unique=True, verbose_name='Имя пользователя дерева', null=True, blank=True)
    courses = models.ManyToManyField('Courses', on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True, blank=True)


class Teacher(models.Model):

    name = models.CharField(max_length=50, unique=True, verbose_name='Имя пользователя дерева', null=True, blank=True)
    courses = models.ManyToManyField('Courses', on_delete=models.CASCADE, null=True, blank=True)
