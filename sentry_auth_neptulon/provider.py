from __future__ import absolute_import, print_function

from sentry.auth.providers.oauth2 import OAuth2Callback, OAuth2Provider, OAuth2Login
from .constants import AUTHORIZE_URL, ACCESS_TOKEN_URL, CLIENT_ID, CLIENT_SECRET, SCOPE
from .views import FetchUser, NeptulonConfigureView


class NeptulonOAuth2Login(OAuth2Login):
    authorize_url = AUTHORIZE_URL
    client_id = CLIENT_ID
    scope = SCOPE

    def __init__(self):
        super(NeptulonOAuth2Login, self).__init__()

    def get_authorize_params(self, state, redirect_uri):
        params = super(NeptulonOAuth2Login, self).get_authorize_params(
            state, redirect_uri
        )
        # TODO(dcramer): ideally we could look at the current resulting state
        # when an existing auth happens, and if they're missing a refresh_token
        # we should re-prompt them a second time with ``approval_prompt=force``
        # params['approval_prompt'] = 'force'
        params['access_type'] = 'offline'
        return params


class NeptulonOAuth2Provider(OAuth2Provider):
    name = 'Neptulon'
    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET

    def __init__(self, **config):
        super(NeptulonOAuth2Provider, self).__init__(**config)

    def get_configure_view(self):
        return NeptulonConfigureView.as_view()

    def get_auth_pipeline(self):
        return [
            NeptulonOAuth2Login(),
            OAuth2Callback(
                access_token_url=ACCESS_TOKEN_URL,
                client_id=self.client_id,
                client_secret=self.client_secret,
            ),
            FetchUser(),
        ]

    def get_refresh_token_url(self):
        return ACCESS_TOKEN_URL

    def build_config(self, state):
        # TODO(dcramer): we actually want to enforce a domain here. Should that
        # be a view which does that, or should we allow this step to raise
        # validation errors?
        return {}

    def build_identity(self, state):
        # data.user => {
        #   "displayName": "David Cramer",
        #   "emails": [{"value": "david@getsentry.com", "type": "account"}],
        #   "domain": "getsentry.com",
        #   "verified": false
        # }
        data = state['data']
        user_data = state['user']
        return {
            'id': user_data['id'],
            # TODO: is there a "correct" email?
            'email': user_data['email'],
            'name': user_data['name'],
            'data': self.get_oauth_data(data),
        }
