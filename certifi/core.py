# -*- coding: utf-8 -*-

"""
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem or its contents.
"""
import os

def read_text(encoding="ascii"):
    with open(where(), "r", encoding=encoding) as data:
        return data.read()

def where():
    return '/etc/ssl/certs/ca-certificates.crt'


def contents():
    return read_text(encoding="ascii")
