from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from userauths.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'bio', 'date_joined']

admin.site.register(User, UserAdmin)