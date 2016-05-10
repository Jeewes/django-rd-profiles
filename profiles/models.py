# -*- coding: utf-8 -*-
import hashlib
import urllib

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from easy_thumbnails.files import get_thumbnailer


class User(AbstractUser):
    """
    Normal django User model with some additional fields
    """
    profile_photo = models.ImageField(
        blank=True,
        upload_to="profile_photos/",
        verbose_name=_("profile photo")
    )

    def get_profile_image(self, size_alias='avatar'):
        if self.profile_photo:
            return get_thumbnailer(self.profile_photo)[size_alias].url
        size = settings.THUMBNAIL_ALIASES[''][size_alias]['size'][0]
        return "http://www.gravatar.com/avatar/%s?%s" % (
            hashlib.md5(self.email.lower().encode('utf-8')).hexdigest(),
            urllib.parse.urlencode({"d": "retro", "s": size})
        )

# Change blank setting inherited from parent class
User._meta.get_field('email').blank = False


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

