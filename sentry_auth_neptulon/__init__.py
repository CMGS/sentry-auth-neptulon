from __future__ import absolute_import

from sentry.auth import register

from .provider import NeptulonOAuth2Provider

register('neptulon', NeptulonOAuth2Provider)
