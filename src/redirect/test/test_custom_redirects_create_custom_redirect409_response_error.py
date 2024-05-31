# coding: utf-8

"""
    BloxOne Redirect API

    You can configure BloxOne Threat Defense Cloud to redirect traffic to the Infoblox server that displays the default or customized redirect page. You can redirect traffic to a custom destination using custom redirects. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from redirect.models.custom_redirects_create_custom_redirect409_response_error import CustomRedirectsCreateCustomRedirect409ResponseError


class TestCustomRedirectsCreateCustomRedirect409ResponseError(
        unittest.TestCase):
    """CustomRedirectsCreateCustomRedirect409ResponseError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> CustomRedirectsCreateCustomRedirect409ResponseError:
        """Test CustomRedirectsCreateCustomRedirect409ResponseError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomRedirectsCreateCustomRedirect409ResponseError`
        """
        model = CustomRedirectsCreateCustomRedirect409ResponseError()
        if include_optional:
            return CustomRedirectsCreateCustomRedirect409ResponseError(
                code = 'ALREADY_EXISTS',
                message = 'Custom Redirect with name 'custom_redirect_ip_address_1' already exists',
                status = '409'
            )
        else:
            return CustomRedirectsCreateCustomRedirect409ResponseError(
        )
        """

    def testCustomRedirectsCreateCustomRedirect409ResponseError(self):
        """Test CustomRedirectsCreateCustomRedirect409ResponseError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()