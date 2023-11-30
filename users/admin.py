from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import LocalUser

# Register your models here.

class LocalUserAdmin(UserAdmin):
    model = LocalUser
    list_display = ['username']



admin.site.register(LocalUser, LocalUserAdmin)