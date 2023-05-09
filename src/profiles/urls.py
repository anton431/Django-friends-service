from django.urls import path

from profiles.views import ProfilesHome, FindFriends, my_profile_view, Applications, login, RegisterUser

urlpatterns = [
    path('', ProfilesHome.as_view(), name='home'),
    path('find_friends/', FindFriends.as_view(), name='find_friends'),
    path('my_friends/', my_profile_view, name='my_friends'),
    path('applications/', Applications.as_view(), name='applications'),
    path('login/', login, name='login'),
    path('register', RegisterUser.as_view(), name='register'),
]