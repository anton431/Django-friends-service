from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from profiles.models import Profile

# Create your views here.


menu = [
        {'title': 'Найти друзей', 'url_name': 'find_friends'},
        {'title': 'Список друзей', 'url_name': 'my_friends'},
        {'title':'Входящие/исходящие', 'url_name': 'applications'},
        ]

exit = {'exit': 'Войти', 'url_name': 'login'}

class ProfilesHome(ListView):
    model = Profile
    template_name = 'profiles/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['exit'] = exit
        return context

def find_friends(request):
    return HttpResponse("Искать друзей")

def my_friends(request):
    return HttpResponse("Мои друзья")

def applications(request):
    return HttpResponse("Заявки")

def login(request):
    return HttpResponse('Войти')
