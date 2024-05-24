# coding: utf-8

"""
    BloxOne Redirect API

    You can configure BloxOne Threat Defense Cloud to redirect traffic to the Infoblox server that displays the default or customized redirect page. You can redirect traffic to a custom destination using custom redirects. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from redirect.models.certificate_get_proxy_certificates500_response import CertificateGetProxyCertificates500Response


class TestCertificateGetProxyCertificates500Response(unittest.TestCase):
    """CertificateGetProxyCertificates500Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
            self,
            include_optional) -> CertificateGetProxyCertificates500Response:
        """Test CertificateGetProxyCertificates500Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificateGetProxyCertificates500Response`
        """
        model = CertificateGetProxyCertificates500Response()
        if include_optional:
            return CertificateGetProxyCertificates500Response(
                error = redirect.models.certificate_get_proxy_certificates_500_response_error.certificateGetProxyCertificates_500_response_error(
                    code = 'INTERNAL', 
                    message = 'Internal Server Error', 
                    status = '500', )
            )
        else:
            return CertificateGetProxyCertificates500Response(
        )
        """

    def testCertificateGetProxyCertificates500Response(self):
        """Test CertificateGetProxyCertificates500Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
