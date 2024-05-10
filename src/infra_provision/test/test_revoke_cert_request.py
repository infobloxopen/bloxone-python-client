# coding: utf-8

"""
    Host Activation Service

    Host activation service provides a RESTful interface to manage cert and join token object. Join tokens are essentially a password that allows on-prem hosts to auto-associate themselves to a customer's account and receive a signed cert.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from infra_provision.models.revoke_cert_request import RevokeCertRequest


class TestRevokeCertRequest(unittest.TestCase):
    """RevokeCertRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RevokeCertRequest:
        """Test RevokeCertRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RevokeCertRequest`
        """
        model = RevokeCertRequest()
        if include_optional:
            return RevokeCertRequest(
                cert_serial = '',
                ophid = '',
                revoke_reason = ''
            )
        else:
            return RevokeCertRequest(
        )
        """

    def testRevokeCertRequest(self):
        """Test RevokeCertRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
