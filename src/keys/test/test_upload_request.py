# coding: utf-8

"""
    DDI Keys API

    The DDI Keys application is a BloxOne DDI service for managing TSIG keys and GSS-TSIG (Kerberos) keys which are used by other BloxOne DDI applications. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from keys.models.upload_request import UploadRequest


class TestUploadRequest(unittest.TestCase):
    """UploadRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UploadRequest:
        """Test UploadRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UploadRequest`
        """
        model = UploadRequest()
        if include_optional:
            return UploadRequest(
                comment = '',
                content = 'aGVsbG93b3JsZA==',
                fields = keys.models.`field_mask`_represents_a_set_of_symbolic_field_paths,_for_example:.`FieldMask` represents a set of symbolic field paths, for example:(
                    paths = [
                        ''
                        ], ),
                tags = None,
                type = 'UNKNOWN'
            )
        else:
            return UploadRequest(
                content = 'aGVsbG93b3JsZA==',
                type = 'UNKNOWN',
        )
        """

    def testUploadRequest(self):
        """Test UploadRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
