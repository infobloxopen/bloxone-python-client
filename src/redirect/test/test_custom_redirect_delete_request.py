# coding: utf-8

"""
    BloxOne Redirect API

    You can configure BloxOne Threat Defense Cloud to redirect traffic to the Infoblox server that displays the default or customized redirect page. You can redirect traffic to a custom destination using custom redirects. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from redirect.models.custom_redirect_delete_request import CustomRedirectDeleteRequest


class TestCustomRedirectDeleteRequest(unittest.TestCase):
    """CustomRedirectDeleteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomRedirectDeleteRequest:
        """Test CustomRedirectDeleteRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomRedirectDeleteRequest`
        """
        model = CustomRedirectDeleteRequest()
        if include_optional:
            return CustomRedirectDeleteRequest(
                ids = [12345, 53215]
            )
        else:
            return CustomRedirectDeleteRequest(
        )
        """

    def testCustomRedirectDeleteRequest(self):
        """Test CustomRedirectDeleteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
