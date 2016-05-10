# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import UpdateView

from rest_framework import viewsets

from .models import UserSerializer


class ProfileView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    fields = ["last_name", "first_name", "profile_photo"]
    template_name = "profiles/detail.jinja"

    def get_object(self, queryset=None):
        return self.request.user


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    fields = ["last_name", "first_name", "profile_photo"]
    template_name = "profiles/edit.jinja"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        messages.success(
            self.request,
            _("Your profile was saved successfully.")
        )
        return reverse("profiles:show")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all().order_by('-date_joined')
    serializer_class = UserSerializer