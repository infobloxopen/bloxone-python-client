# coding: utf-8

"""
    DDI Keys API

    The DDI Keys application is a BloxOne DDI service for managing TSIG keys and GSS-TSIG (Kerberos) keys which are used by other BloxOne DDI applications. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from keys.models.tsig_key import TSIGKey


class TestTSIGKey(unittest.TestCase):
    """TSIGKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TSIGKey:
        """Test TSIGKey
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TSIGKey`
        """
        model = TSIGKey()
        if include_optional:
            return TSIGKey(
                algorithm = '',
                comment = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                name = 'test.key.com.',
                protocol_name = '',
                secret = 'bGVzYnJvbnplc2ZvbnRkdXNraQ==',
                tags = keys.models.tags.tags(),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return TSIGKey(
                name = 'test.key.com.',
                secret = 'bGVzYnJvbnplc2ZvbnRkdXNraQ==',
        )
        """

    def testTSIGKey(self):
        """Test TSIGKey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
