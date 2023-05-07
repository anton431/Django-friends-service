from django.contrib import admin
from profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','username','user')
    list_display_links = ('id', 'username')
    search_fields = ('username',)
    prepopulated_fields = {'slug':('username',)}


admin.site.register(Profile, ProfileAdmin)
