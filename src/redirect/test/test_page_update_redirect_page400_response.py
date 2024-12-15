# coding: utf-8

"""
    BloxOne Redirect API

    You can configure BloxOne Threat Defense Cloud to redirect traffic to the Infoblox server that displays the default or customized redirect page. You can redirect traffic to a custom destination using custom redirects. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from redirect.models.page_update_redirect_page400_response import PageUpdateRedirectPage400Response


class TestPageUpdateRedirectPage400Response(unittest.TestCase):
    """PageUpdateRedirectPage400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self,
                      include_optional) -> PageUpdateRedirectPage400Response:
        """Test PageUpdateRedirectPage400Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageUpdateRedirectPage400Response`
        """
        model = PageUpdateRedirectPage400Response()
        if include_optional:
            return PageUpdateRedirectPage400Response(
                error = redirect.models.redirect_page_update_redirect_page_400_response_error.redirect_pageUpdateRedirectPage_400_response_error(
                    code = 'INVALID_ARGUMENT', 
                    message = ''type' must not be empty', 
                    status = '400', )
            )
        else:
            return PageUpdateRedirectPage400Response(
        )
        """

    def testPageUpdateRedirectPage400Response(self):
        """Test PageUpdateRedirectPage400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()