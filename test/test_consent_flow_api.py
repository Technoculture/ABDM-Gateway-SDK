# coding: utf-8

"""
    Gateway

    Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing 

    The version of the OpenAPI document: 0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abdm_gateway.api.consent_flow_api import ConsentFlowApi


class TestConsentFlowApi(unittest.TestCase):
    """ConsentFlowApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConsentFlowApi()

    def tearDown(self) -> None:
        pass

    def test_v05_consent_requests_init_post(self) -> None:
        """Test case for v05_consent_requests_init_post

        Create consent request
        """
        pass

    def test_v05_consent_requests_on_init_post(self) -> None:
        """Test case for v05_consent_requests_on_init_post

        Response to consent request
        """
        pass

    def test_v05_consent_requests_on_status_post(self) -> None:
        """Test case for v05_consent_requests_on_status_post

        Result of consent request status
        """
        pass

    def test_v05_consent_requests_status_post(self) -> None:
        """Test case for v05_consent_requests_status_post

        Get consent request status
        """
        pass

    def test_v05_consents_fetch_post(self) -> None:
        """Test case for v05_consents_fetch_post

        Get consent artefact
        """
        pass

    def test_v05_consents_hip_notify_post(self) -> None:
        """Test case for v05_consents_hip_notify_post

        Consent notification
        """
        pass

    def test_v05_consents_hip_on_notify_post(self) -> None:
        """Test case for v05_consents_hip_on_notify_post

        Consent notification
        """
        pass

    def test_v05_consents_hiu_notify_post(self) -> None:
        """Test case for v05_consents_hiu_notify_post

        Consent notification
        """
        pass

    def test_v05_consents_hiu_on_notify_post(self) -> None:
        """Test case for v05_consents_hiu_on_notify_post

        Consent notification
        """
        pass

    def test_v05_consents_on_fetch_post(self) -> None:
        """Test case for v05_consents_on_fetch_post

        Result of fetch request for a consent artefact
        """
        pass


if __name__ == '__main__':
    unittest.main()