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

STATUS_CHOICES = (
    ('send', 'Отправить'),
    ('accepted', 'Принять')
)

class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender', verbose_name='Отправитель')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver', verbose_name='Получатель')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, verbose_name='Статус')

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"

    class Meta:
        verbose_name = 'Отношения'
        verbose_name_plural = 'Отношения'


