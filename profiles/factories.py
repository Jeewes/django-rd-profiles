# -*- coding: utf-8 -*-
from factory.django import DjangoModelFactory
from faker import Factory

from . import models


faker = Factory.create()


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
    first_name = faker.first_name()
    last_name = faker.last_name()
    email = "%s.%s@example.com" % (first_name, last_name)


class AdminFactory(UserFactory):
    is_superuser = True
    is_staff = True
