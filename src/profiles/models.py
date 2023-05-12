from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q


class ProfileManager(models.Manager):
    def get_all_profiles_to_invite(self, sender):
        profiles = Profile.objects.all().exclude(user=sender)
        profile = Profile.objects.get(user=sender)
        qs = Relationship.objects.filter(Q(sender=profile) | Q(receiver=profile))
        accepted = set([])
        for rel in qs:
            if rel.status == 'accepted':
                accepted.add(rel.receiver)
                accepted.add(rel.sender)
        available = [profile for profile in profiles if profile not in accepted]
        return available

    def get_all_profiles(self, me):
        profiles = Profile.objects.all().exclude(user=me)
        return profiles

class Profile(models.Model):
    username = models.CharField(max_length=200, blank=True, unique=True, verbose_name='Имя Пользователя')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    avatar = models.ImageField(default='avatar.png', upload_to="avatar/%Y/%m/%d/", verbose_name='Аватар')
    friends = models.ManyToManyField(User, blank=True, related_name='friends', verbose_name='Друзья')
    slug = models.SlugField(unique=True, blank=True,verbose_name='URL')

    objects = ProfileManager()

    def __str__(self):
        return self.username

    def get_friends(self):
        return self.friends.all()

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
        ordering = ['username',]

STATUS_CHOICES = (
    ('send', 'Отправить'),
    ('accepted', 'Принять')
)

class RelationshipManager(models.Manager):
    def invatations_received(self, receiver):
        qs = Relationship.objects.filter(receiver=receiver, status='send')
        return qs

    def invatations_sended(self, sender):
        qw = Relationship.objects.filter(sender=sender, status='send')
        return qw

class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender', verbose_name='Отправитель')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver', verbose_name='Получатель')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, verbose_name='Статус')

    objects = RelationshipManager()

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"

    class Meta:
        verbose_name = 'Отношения'
        verbose_name_plural = 'Отношения'


