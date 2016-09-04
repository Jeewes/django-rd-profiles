# -*- coding: utf-8 -*-
import factory
from django.utils.text import slugify
from factory.django import DjangoModelFactory

from . import models


class UserFactory(DjangoModelFactory):
    class Meta:
        model = models.User

    first_name = 'John'
    last_name = 'Doe'
    username = 'john_doe'
    email = 'john@example.com'
    password = 'password'

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """
        Override the default ``_create`` with our custom call.
        Docs: http://factoryboy.readthedocs.org/en/latest/recipes.html#custom-manager-methods
        """
        manager = cls._get_manager(model_class)
        # The default would use ``manager.create(*args, **kwargs)``
        return manager.create_user(*args, **kwargs)


class RandomUserFactory(UserFactory):
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.LazyAttribute(
        lambda user: ("%s.%s@example.com" % (user.first_name, user.last_name)).lower()
    )
    username = factory.LazyAttribute(
        lambda user: slugify("%s%s" % (user.first_name, user.last_name))
    )

class AdminFactory(UserFactory):
    is_superuser = True
    is_staff = True
