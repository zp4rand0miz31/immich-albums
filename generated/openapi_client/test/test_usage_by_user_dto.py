# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.79.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.usage_by_user_dto import UsageByUserDto  # noqa: E501

class TestUsageByUserDto(unittest.TestCase):
    """UsageByUserDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsageByUserDto:
        """Test UsageByUserDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsageByUserDto`
        """
        model = UsageByUserDto()  # noqa: E501
        if include_optional:
            return UsageByUserDto(
                photos = 56,
                usage = 56,
                user_first_name = '',
                user_id = '',
                user_last_name = '',
                videos = 56
            )
        else:
            return UsageByUserDto(
                photos = 56,
                usage = 56,
                user_first_name = '',
                user_id = '',
                user_last_name = '',
                videos = 56,
        )
        """

    def testUsageByUserDto(self):
        """Test UsageByUserDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()