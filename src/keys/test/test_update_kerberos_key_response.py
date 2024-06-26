# coding: utf-8

"""
    DDI Keys API

    The DDI Keys application is a BloxOne DDI service for managing TSIG keys and GSS-TSIG (Kerberos) keys which are used by other BloxOne DDI applications. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from keys.models.update_kerberos_key_response import UpdateKerberosKeyResponse


class TestUpdateKerberosKeyResponse(unittest.TestCase):
    """UpdateKerberosKeyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateKerberosKeyResponse:
        """Test UpdateKerberosKeyResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateKerberosKeyResponse`
        """
        model = UpdateKerberosKeyResponse()
        if include_optional:
            return UpdateKerberosKeyResponse(
                result = keys.models.key.Key(
                    algorithm = '', 
                    comment = '', 
                    domain = '', 
                    id = '', 
                    principal = '', 
                    tags = keys.models.tags.tags(), 
                    uploaded_at = '', 
                    version = 56, )
            )
        else:
            return UpdateKerberosKeyResponse(
        )
        """

    def testUpdateKerberosKeyResponse(self):
        """Test UpdateKerberosKeyResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
