# -*- coding: utf-8 -*-

import os
import unittest
from unittest.mock import patch, mock_open

import certifi


class TestCertifi(unittest.TestCase):
    def test_cabundle_exists(self):
        assert certifi.where() == '/etc/ssl/certs/ca-certificates.crt'

    def test_read_contents(self):
        with patch("builtins.open", mock_open(read_data="-----BEGIN CERTIFICATE-----")) as mock_file:
            content = certifi.contents()
            assert "-----BEGIN CERTIFICATE-----" in content
            mock_file.assert_called_with("/etc/ssl/certs/ca-certificates.crt", 'r', encoding='ascii')
