from django.urls import path

from profiles.views import ProfilesHome, FindFriends, my_profile_view, invites_received_view, login, RegisterUser, \
    send_invatation, remove_from_friends

urlpatterns = [
    path('', ProfilesHome.as_view(), name='home'),
    path('find_friends/', FindFriends.as_view(), name='find_friends'),
    path('my_friends/', my_profile_view, name='my_friends'),
    path('applications/', invites_received_view, name='applications'),
    path('login/', login, name='login'),
    path('register', RegisterUser.as_view(), name='register'),
    path('send_invite/', send_invatation, name='send-invite'),
    path('remove-friend/', remove_from_friends, name='remove-friend'),
]