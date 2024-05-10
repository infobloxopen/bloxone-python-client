# coding: utf-8

"""
    Host Activation Service

    Host activation service provides a RESTful interface to manage cert and join token object. Join tokens are essentially a password that allows on-prem hosts to auto-associate themselves to a customer's account and receive a signed cert.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from infra_provision.api.uicsr_api import UICSRApi


class TestUICSRApi(unittest.TestCase):
    """UICSRApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UICSRApi()

    def tearDown(self) -> None:
        pass

    def test_Approve(self) -> None:
        """Test case for Approve

        Marks the certificate signing request as approved. The host activation service will then continue with the signing process.
        """
        pass

    def test_Deny(self) -> None:
        """Test case for Deny

        Marks the certificate signing request as denied.
        """
        pass

    def test_List(self) -> None:
        """Test case for List

        User can list the certificate signing requests for an account.
        """
        pass

    def test_Revoke(self) -> None:
        """Test case for Revoke

        Invalidates a certificate by adding it to a certificate revocation list.
        """
        pass

    def test_Revoke2(self) -> None:
        """Test case for Revoke2

        Invalidates a certificate by adding it to a certificate revocation list.
        """
        pass


if __name__ == '__main__':
    unittest.main()
