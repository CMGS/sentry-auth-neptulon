Neptulon Auth for Sentry
======================

An SSO provider for Sentry which enables Neptulon Apps authentication.

Install
-------

::

    $ pip install -e git+https://github.com/CMGS/sentry-auth-neptulon#egg=sentry-auth-neptulon

Setup
-----

Start by `creating a project in the SSO Console <https://sso.neptulon.net>`_.

In the **Authorized redirect URIs** add the SSO endpoint for your installation::

    https://sentry.example.com/auth/sso/

Finally, obtain the API keys and plug them into your ``sentry.conf.py``:

.. code-block:: python

    NEPTULON_TOKEN_URL = ""

    NEPTULON_AUTH_URL = ""

    NEPTULON_CLIENT_ID = ""

    NEPTULON_CLIENT_SECRET = ""

    NEPTULON_USER_DETAILS_URL = ""

