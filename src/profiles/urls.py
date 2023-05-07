from django.urls import path

from profiles.views import ProfilesHome, find_friends, my_friends, applications, login

urlpatterns = [
    path('', ProfilesHome.as_view(), name='home'),
    path('find_friends/', find_friends, name='find_friends'),
    path('my_friends/', my_friends, name='my_friends'),
    path('applications/', applications, name='applications'),
    path('login/', login, name='login'),
]