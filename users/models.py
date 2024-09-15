from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models


class User(AbstractUser):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [(MALE, 'Мужской'),
                      (FEMALE, 'Женский')]
    photo = models.ImageField(verbose_name='Фото', upload_to='images/users/%Y/%m', blank=True, null=True)
    date_birth = models.DateTimeField(verbose_name='Дата рождения', blank=True, null=True)
    gender = models.CharField(verbose_name='Пол', blank=False, null=True, choices=GENDER_CHOICES, default=FEMALE)
    phone = models.CharField(verbose_name='Телефон', blank=False, null=True, unique=True)
    is_active = models.BooleanField(default=False, verbose_name='Активный', null=False)

    role = models.ForeignKey('RoleUser', on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class RoleUser(models.Model):
    title = models.CharField(verbose_name='Роль пользователя', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Роль пользователей'
        verbose_name_plural = 'Роль пользователей'


class Teacher(models.Model):
    teacher = models.ForeignKey(get_user_model(),
                                limit_choices_to={'role__title': 'Учитель'}, on_delete=models.CASCADE,
                                related_name='teacher')
    student = models.ManyToManyField(get_user_model(),
                                     limit_choices_to={'role__title': 'Ученик'}, related_name='student')

    class Meta:
        verbose_name = 'Учителя и их ученики'
        verbose_name_plural = 'Учителя и их ученики'


