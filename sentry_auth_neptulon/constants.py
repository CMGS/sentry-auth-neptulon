from __future__ import absolute_import, print_function

from django.conf import settings

ACCESS_TOKEN_URL = getattr(settings, 'NEPTULON_TOKEN_URL', None)
AUTHORIZE_URL = getattr(settings, 'NEPTULON_AUTH_URL', None)
CLIENT_ID = getattr(settings, 'NEPTULON_CLIENT_ID', None)
CLIENT_SECRET = getattr(settings, 'NEPTULON_CLIENT_SECRET', None)
USER_DETAILS_ENDPOINT = getattr(settings, 'NEPTULON_USER_DETAILS_URL', None)

SCOPE = 'email'
