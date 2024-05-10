# coding: utf-8

"""
    Host Activation Service

    Host activation service provides a RESTful interface to manage cert and join token object. Join tokens are essentially a password that allows on-prem hosts to auto-associate themselves to a customer's account and receive a signed cert.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from infra_provision.models.read_join_token_response import ReadJoinTokenResponse


class TestReadJoinTokenResponse(unittest.TestCase):
    """ReadJoinTokenResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReadJoinTokenResponse:
        """Test ReadJoinTokenResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReadJoinTokenResponse`
        """
        model = ReadJoinTokenResponse()
        if include_optional:
            return ReadJoinTokenResponse(
                result = infra_provision.models.hostactivation_join_token.hostactivationJoinToken(
                    deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    description = '', 
                    expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', 
                    last_used_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    name = '', 
                    status = 'UNKNOWN', 
                    tags = infra_provision.models.tags.tags(), 
                    token_id = '', 
                    use_counter = 56, )
            )
        else:
            return ReadJoinTokenResponse(
        )
        """

    def testReadJoinTokenResponse(self):
        """Test ReadJoinTokenResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
