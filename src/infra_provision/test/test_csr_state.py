# coding: utf-8

"""
    Host Activation Service

    Host activation service provides a RESTful interface to manage cert and join token object. Join tokens are essentially a password that allows on-prem hosts to auto-associate themselves to a customer's account and receive a signed cert.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from infra_provision.models.csr_state import CSRState


class TestCSRState(unittest.TestCase):
    """CSRState unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCSRState(self):
        """Test CSRState"""
        # inst = CSRState()


if __name__ == '__main__':
    unittest.main()
