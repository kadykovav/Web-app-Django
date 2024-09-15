# from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# from django.utils.text import slugify


class BlogPost(models.Model):
    DRAFT = 0
    PUBLISHED = 1
    PUBLISHED_CHOICES = [
        (DRAFT, 'Черновик'),
        (PUBLISHED, 'Опубликовано')
    ]
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.CharField(max_length=255, blank=True, verbose_name='Краткое описание')
    content = models.TextField(null=False, blank=False, verbose_name='Содержание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    image = models.ImageField(upload_to='images/posts/%Y/%m/', default=None, blank=True, null=True,
                              verbose_name='Изображение')

    published = models.BooleanField(default=DRAFT, verbose_name='Опубликовать',
                                    choices=tuple(map(lambda x: (bool(x[0]), x[1]), PUBLISHED_CHOICES)))
    slug = models.SlugField(max_length=100, verbose_name='Слаг')
    themes = models.ManyToManyField('ThemePost', blank=True, related_name='themes', verbose_name='Темы')

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'


#
class ThemePost(models.Model):
    theme = models.CharField(max_length=100, verbose_name='Темы')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Темы постов'
        verbose_name_plural = 'Темы постов'
