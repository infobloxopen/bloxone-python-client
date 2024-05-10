# coding: utf-8

"""
    Host Activation Service

    Host activation service provides a RESTful interface to manage cert and join token object. Join tokens are essentially a password that allows on-prem hosts to auto-associate themselves to a customer's account and receive a signed cert.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from infra_provision.models.delete_join_tokens_request import DeleteJoinTokensRequest


class TestDeleteJoinTokensRequest(unittest.TestCase):
    """DeleteJoinTokensRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteJoinTokensRequest:
        """Test DeleteJoinTokensRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteJoinTokensRequest`
        """
        model = DeleteJoinTokensRequest()
        if include_optional:
            return DeleteJoinTokensRequest(
                ids = [
                    ''
                    ]
            )
        else:
            return DeleteJoinTokensRequest(
        )
        """

    def testDeleteJoinTokensRequest(self):
        """Test DeleteJoinTokensRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
