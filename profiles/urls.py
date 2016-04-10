# -*- coding: utf-8 -*-
"""
Profile management related urls
"""
from django.conf.urls import url

from .views import ProfileView, EditProfileView


urlpatterns = [
    url(r'^$', ProfileView.as_view(), name='show'),
    url(r'^edit/$', EditProfileView.as_view(), name="edit"),
]
