test:
	pip install -e .
	pip install "file://`pwd`#egg=sentry-auth-neptulon[tests]"
	py.test -x
