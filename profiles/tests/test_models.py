# -*- coding: utf-8 -*-
import pytest

from profiles.factories import UserFactory


@pytest.mark.django_db
def test_fallback_to_gravatar():
    user = UserFactory.build(profile_photo="")
    image_url = user.get_profile_image()
    assert "gravatar.com" in image_url
