from django.contrib.auth import get_user_model
from django.db import models

from .constans import TEXT_LIMIT, MAX_LENGTH


User = get_user_model()


class Car(models.Model):
    '''Model for cars.'''
    make = models.CharField(max_length=MAX_LENGTH, verbose_name='Марка')
    model = models.CharField(max_length=MAX_LENGTH, verbose_name='Модель')
    year = models.IntegerField(
        blank=True, null=True, verbose_name='Год выпуска'
    )
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
        verbose_name='Обновлено'
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Владелец автомобиля'
    )

    class Meta:
        ordering = ('-updated_at', '-created_at')
        default_related_name = 'cars'
        verbose_name = 'автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return f'{self.make[:TEXT_LIMIT]}'


class Comment(models.Model):
    '''Model for comments.'''
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Добавлено'
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.make[:TEXT_LIMIT]}'
