from django.urls import path

from profiles.views import ProfilesHome, profiles_list_view, my_profile_view, invites_received_view, login, RegisterUser

urlpatterns = [
    path('', ProfilesHome.as_view(), name='home'),
    path('find_friends/', profiles_list_view, name='find_friends'),
    path('my_friends/', my_profile_view, name='my_friends'),
    path('applications/', invites_received_view, name='applications'),
    path('login/', login, name='login'),
    path('register', RegisterUser.as_view(), name='register'),
]