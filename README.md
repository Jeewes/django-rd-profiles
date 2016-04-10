# Profiles for Django

This app provides a custom user model with common user profile features like:
- Profile editing

## Installation

1. Install `<todo>`
2. Add `"profiles"` to your `INSTALLED_APPS`.
3. Set `AUTH_USER_MODEL = "profiles.User"`
4. Add `url(r'^profile/', include('profiles.urls', namespace="profiles")),` to your urls.
