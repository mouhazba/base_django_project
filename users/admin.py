from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


# Register your models here.
from .forms import CustomUserForm, CustomUserFormChange


CustomeUser = get_user_model()

class CutomeUserAdmin(UserAdmin):
    add_form = CustomUserForm

    form = CustomUserFormChange

    model= CustomeUser
    list_display= ['username', 'password',]


admin.site.register(CustomeUser, CutomeUserAdmin)