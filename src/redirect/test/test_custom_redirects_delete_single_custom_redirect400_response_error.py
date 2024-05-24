# coding: utf-8

"""
    BloxOne Redirect API

    You can configure BloxOne Threat Defense Cloud to redirect traffic to the Infoblox server that displays the default or customized redirect page. You can redirect traffic to a custom destination using custom redirects. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from redirect.models.custom_redirects_delete_single_custom_redirect400_response_error import CustomRedirectsDeleteSingleCustomRedirect400ResponseError


class TestCustomRedirectsDeleteSingleCustomRedirect400ResponseError(
        unittest.TestCase):
    """CustomRedirectsDeleteSingleCustomRedirect400ResponseError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> CustomRedirectsDeleteSingleCustomRedirect400ResponseError:
        """Test CustomRedirectsDeleteSingleCustomRedirect400ResponseError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomRedirectsDeleteSingleCustomRedirect400ResponseError`
        """
        model = CustomRedirectsDeleteSingleCustomRedirect400ResponseError()
        if include_optional:
            return CustomRedirectsDeleteSingleCustomRedirect400ResponseError(
                code = 'INVALID_ARGUMENT',
                message = 'invalid 'id': value must be greater than or equal to 0',
                status = '400'
            )
        else:
            return CustomRedirectsDeleteSingleCustomRedirect400ResponseError(
        )
        """

    def testCustomRedirectsDeleteSingleCustomRedirect400ResponseError(self):
        """Test CustomRedirectsDeleteSingleCustomRedirect400ResponseError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
