# coding: utf-8

"""
Gateway

Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing

The version of the OpenAPI document: 0.5
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from abdm_gateway.models.share_profile_result1 import ShareProfileResult1


class TestShareProfileResult1(unittest.TestCase):
    """ShareProfileResult1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ShareProfileResult1:
        """Test ShareProfileResult1
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ShareProfileResult1`
        """
        model = ShareProfileResult1()
        if include_optional:
            return ShareProfileResult1(
                request_id = '5f7a535d-a3fd-416b-b069-c97d021fbacd',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                acknowledgement = abdm_gateway.models.share_profile_acknowledgement1.ShareProfileAcknowledgement1(
                    status = 'SUCCESS', 
                    health_id = '<username>@<suffix>', 
                    token_number = '', ),
                error = abdm_gateway.models.error.Error(
                    code = 1000, 
                    message = '', ),
                resp = abdm_gateway.models.request_reference.RequestReference(
                    request_id = '', )
            )
        else:
            return ShareProfileResult1(
                request_id = '5f7a535d-a3fd-416b-b069-c97d021fbacd',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                acknowledgement = abdm_gateway.models.share_profile_acknowledgement1.ShareProfileAcknowledgement1(
                    status = 'SUCCESS', 
                    health_id = '<username>@<suffix>', 
                    token_number = '', ),
                resp = abdm_gateway.models.request_reference.RequestReference(
                    request_id = '', ),
        )
        """

    def testShareProfileResult1(self):
        """Test ShareProfileResult1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
