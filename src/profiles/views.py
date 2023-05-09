from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from profiles.forms import RegisterUserForm
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



class FindFriends(LoginRequiredMixin,DataMixin, ListView):
    model = Profile
    template_name = 'profiles/find_friends.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Найти друзей")
        return dict(list(context.items()) + list(c_def.items()))


class MyFriends(LoginRequiredMixin,DataMixin, ListView):
    model = Profile
    template_name = 'profiles/my_friends.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Мои друзья")
        return dict(list(context.items()) + list(c_def.items()))

class Applications(LoginRequiredMixin,DataMixin, ListView):
    model = Profile
    template_name = 'profiles/applications.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Заявки")
        return dict(list(context.items()) + list(c_def.items()))

def login(request):
    return HttpResponse('Войти')

class RegisterUser(DataMixin,CreateView):
    form_class = UserCreationForm
    template_name = 'profiles/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
