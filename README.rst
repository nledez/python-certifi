.. image:: https://github.com/nledez/python-certifi-debian/workflows/CI/badge.svg
   :target: https://github.com/nledez/python-certifi-debian/actions
   :alt: CI

.. image:: https://readthedocs.org/projects/certifi-debian/badge/?version=latest
   :target: https://certifi-debian.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

Certifi-debian: Python SSL Certificates for Debian like
=======================================================

`Certifi-debian` provides a fork of https://github.com/certifi/python-certifi but use
distro bundle for validating the trustworthiness of SSL certificates while
verifying the identity of TLS hosts. It has been extracted from the `Requests`
project.

Installation
------------

``certifi-debian`` can't be available on PyPI. Simply install it with ``pip`` and git URL::

    $ pip install git+https://github.com/nledez/python-certifi-debian

Or add `git+https://github.com/nledez/python-certifi-debian` to your `requirements.txt` BEFORE
`requests` or any lib can use `certifi`.

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
