from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Timetable(models.Model):
    start = models.DateTimeField(verbose_name='Начало', null=False, blank=False, )
    end = models.DateTimeField(verbose_name='Конец', null=False, blank=False, )
    teacher = models.ForeignKey(get_user_model(),
                                limit_choices_to={'role__title': 'Учитель'},
                                on_delete=models.CASCADE,
                                related_name='teacher_timetable', null=False, blank=False)
    student = models.ForeignKey(get_user_model(),
                                limit_choices_to={'role__title': 'Ученик'},
                                related_name='student_timetable',
                                on_delete=models.CASCADE, null=False, blank=False,
                                )
    comment = models.TextField(max_length=1000, verbose_name='Комментарий', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('timetable:lesson_detail', kwargs={'pk': self.pk})
