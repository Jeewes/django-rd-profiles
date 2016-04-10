# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _

from .models import User


class ExtendedUserChangeForm(UserChangeForm):
    """
    Djangos default form with profile fields
    """

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'is_active',
            'is_staff',
            'profile_photo',
        )


@admin.register(User)
class ExtendedUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = ExtendedUserChangeForm
    add_form = UserCreationForm

    list_display = (
        'email',
        'last_name',
        'first_name',
        'is_staff',
        'date_joined',
    )
    date_hierarchy = 'date_joined'
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (
            _('Personal info'),
            {'fields': ('first_name', 'last_name', 'profile_photo',)}
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions'
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2')
            }
        ),
    )
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
