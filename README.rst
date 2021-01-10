Certifi: Python SSL Certificates for Debian like
================================================

`Certifi-debian` provides a fork of https://github.com/certifi/python-certifi but use
distro bundle for validating the trustworthiness of SSL certificates while
verifying the identity of TLS hosts. It has been extracted from the `Requests`
project.

Installation
------------

``certifi-debian`` is available on PyPI. Simply install it with ``pip``::

    $ pip install certifi-debian

Usage
-----

To reference the installed certificate authority (CA) bundle, you can use the
built-in function::

    >>> import certifi

    >>> certifi.where()
    '/etc/ssl/certs/ca-certificates.crt'

Or from the command line::

    $ python -m certifi
    /etc/ssl/certs/ca-certificates.crt

Enjoy!
