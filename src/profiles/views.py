from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from profiles.models import Profile
from profiles.utils import DataMixin


# Create your views here.




class ProfilesHome(DataMixin,ListView):
    model = Profile
    template_name = 'base.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))



class FindFriends(DataMixin, ListView):
    model = Profile
    template_name = 'profiles/find_friends.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Найти друзей")
        return dict(list(context.items()) + list(c_def.items()))


class MyFriends(DataMixin, ListView):
    model = Profile
    template_name = 'profiles/my_friends.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Мои друзья")
        return dict(list(context.items()) + list(c_def.items()))

class Applications(DataMixin, ListView):
    model = Profile
    template_name = 'profiles/applications.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Заявки")
        return dict(list(context.items()) + list(c_def.items()))

def login(request):
    return HttpResponse('Войти')
