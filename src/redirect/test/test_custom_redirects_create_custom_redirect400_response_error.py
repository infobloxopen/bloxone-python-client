# coding: utf-8

"""
    BloxOne Redirect API

    You can configure BloxOne Threat Defense Cloud to redirect traffic to the Infoblox server that displays the default or customized redirect page. You can redirect traffic to a custom destination using custom redirects. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from redirect.models.custom_redirects_create_custom_redirect400_response_error import CustomRedirectsCreateCustomRedirect400ResponseError


class TestCustomRedirectsCreateCustomRedirect400ResponseError(
        unittest.TestCase):
    """CustomRedirectsCreateCustomRedirect400ResponseError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> CustomRedirectsCreateCustomRedirect400ResponseError:
        """Test CustomRedirectsCreateCustomRedirect400ResponseError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomRedirectsCreateCustomRedirect400ResponseError`
        """
        model = CustomRedirectsCreateCustomRedirect400ResponseError()
        if include_optional:
            return CustomRedirectsCreateCustomRedirect400ResponseError(
                code = 'INVALID_ARGUMENT',
                message = ''name' must not be empty',
                status = '400'
            )
        else:
            return CustomRedirectsCreateCustomRedirect400ResponseError(
        )
        """

    def testCustomRedirectsCreateCustomRedirect400ResponseError(self):
        """Test CustomRedirectsCreateCustomRedirect400ResponseError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
