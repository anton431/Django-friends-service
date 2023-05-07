from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=200, blank=True, unique=True, verbose_name='Имя Пользователя')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    avatar = models.ImageField(default='avatar.png', upload_to="avatar/%Y/%m/%d/", verbose_name='Аватар')
    friends = models.ManyToManyField(User, blank=True, related_name='friends', verbose_name='Друзья')
    slug = models.SlugField(unique=True, blank=True,verbose_name='URL')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
        ordering = ['username',]
