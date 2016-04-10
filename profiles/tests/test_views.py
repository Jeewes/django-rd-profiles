# -*- coding: utf-8 -*-
import pytest

from django.conf import settings
from django.core.urlresolvers import reverse

from profiles.factories import RandomUserFactory


@pytest.fixture
@pytest.mark.client
def random_logged_in_user(client):
    user = RandomUserFactory.create(password='pwd')
    client.login(username=user.username, password='pwd')
    return user


@pytest.mark.client
@pytest.mark.django_db
class TestProfilePages:
    profile_page = reverse('profiles:show')
    profile_edit_page = reverse('profiles:edit')

    @pytest.mark.parametrize('url_name', ['show', 'edit'])
    def test_profile_pages_require_login(self, client, url_name):
        response = client.get(reverse('profiles:%s' % url_name))
        assert response.url.startswith(settings.LOGIN_URL)

    def test_edit_profile(self, client, random_logged_in_user):
        assert random_logged_in_user.first_name != 'NewName'
        client.post(
            self.profile_edit_page,
            data={'first_name': 'NewName'}, follow=True
        )
        random_logged_in_user.refresh_from_db()
        assert random_logged_in_user.first_name == 'NewName'
