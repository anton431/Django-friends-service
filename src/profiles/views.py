from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from profiles.forms import RegisterUserForm
from profiles.models import Profile, Relationship
from profiles.utils import DataMixin


# Create your views here.




class ProfilesHome(DataMixin,ListView):
    model = Profile
    template_name = 'base.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))


def profiles_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles(user)
    context = {'qs': qs}
    return render(request, 'profiles/find_friends.html', context)

class FindFriends(LoginRequiredMixin,DataMixin, ListView):
    model = Profile
    template_name = 'profiles/find_friends.html'
    login_url = reverse_lazy('login')
    context_object_name = 'qs'

    def get_queryset(self):
        qs = Profile.objects.get_all_profiles(self.request.user)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        rel_r = Relationship.objects.filter(sender=profile)
        rel_s = Relationship.objects.filter(receiver=profile)
        rel_receiver = []
        rel_sender = []
        for item in rel_r:
            rel_receiver.append(item.receiver.user)
        for item in rel_s:
            rel_sender.append(item.sender.user)
        context["rel_receiver"] = rel_receiver
        context["rel_sender"] = rel_sender
        c_def = self.get_user_context(title="Найти друзей")
        return dict(list(context.items()) + list(c_def.items()))

def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile,}
    return render(request,'profiles/my_friends.html', context)

# class MyFriends(LoginRequiredMixin,DataMixin, ListView):
#     model = Profile
#     template_name = 'profiles/my_friends.html'
#     login_url = reverse_lazy('login')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Мои друзья")
#         return dict(list(context.items()) + list(c_def.items()))

def invites_received_view(request):
    profile = Profile.objects.get(user=request.user)
    qs = Relationship.objects.invatations_received(profile)
    qw = Relationship.objects.invatations_sended(profile)
    results = list(map(lambda x: x.sender, qs))
    resultsw = list(map(lambda x: x.receiver, qw))
    context = {
        'qs': results,
        'qw': resultsw,
    }
    return render(request, 'profiles/applications.html', context)

def accept_invatation(request):
    if request.method=="POST":
        pk = request.POST.get('profile_pk')
        sender = Profile.objects.get(pk=pk)
        receiver = Profile.objects.get(user=request.user)
        rel = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        if rel.status == 'send':
            rel.status = 'accepted'
            rel.save()
    return redirect('applications')

def reject_invatation(request):
    if request.method=="POST":
        pk = request.POST.get('profile_pk')
        receiver = Profile.objects.get(user=request.user)
        sender = Profile.objects.get(pk=pk)
        rel = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        rel.delete()
    return redirect('applications')

# class Applications(LoginRequiredMixin,DataMixin, ListView):
#     model = Profile
#     template_name = 'profiles/applications.html'
#     login_url = reverse_lazy('login')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Заявки")
#         return dict(list(context.items()) + list(c_def.items()))

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

def send_invatation(request):
    if request.method=='POST':
        pk = request.POST.get('profile_pk')
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        rel = Relationship.objects.create(sender=sender, receiver=receiver, status='send')

        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles:my_friends')

def remove_from_friends(request):
    if request.method=='POST':
        pk = request.POST.get('profile_pk')
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        rel = Relationship.objects.get(
            (Q(sender=sender) & Q(receiver=receiver)) | (Q(sender=receiver) & Q(receiver=sender))
        )
        rel.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles:my_friends')
