import pytest
from unittest.mock import patch, Mock, ANY

from radar import RadarClient
from radar.api import ApiRequester
from radar.endpoints import _Endpoint


@pytest.fixture(scope="module")
def base_endpoint(radar):
    return _Endpoint(radar, radar.api_requester)


class TestBaseEndpoint:
    def test_init(self, base_endpoint):
        assert type(base_endpoint.requester) is ApiRequester
        assert type(base_endpoint._radar) is RadarClient

    @patch("requests.request")
    def test_get(self, mocked_request, base_endpoint):
        BASE_URL = base_endpoint.requester.BASE_URL
        mocked_request.return_value = Mock(status_code=200)

        with patch.object(ApiRequester, "_get_headers") as mock_get_headers:
            # should call requests.request GET v1/test
            # headers are mocked, but should use secret_key
            raw_json = base_endpoint._get("v1/test")
            mocked_request.assert_called_once_with(
                "GET", BASE_URL + "v1/test", data=None, headers=ANY, params=None
            )
            mock_get_headers.assert_called_once_with("secret_key")

    @patch("requests.request")
    def test_get_without_json_key(self, mocked_request, base_endpoint):
        mocked_request.return_value = Mock(
            status_code=200, json=lambda: {"topLevel": {"test": "ok"}}
        )

        # without json_key, _get will return full json payload
        get_resp = base_endpoint._get("v1/test")
        assert get_resp == {"topLevel": {"test": "ok"}}

    @patch("requests.request")
    def test_get_json_key(self, mocked_request, base_endpoint):
        mocked_request.return_value = Mock(
            status_code=200, json=lambda: {"topLevel": {"test": "ok"}}
        )

        # with json_key, _get will return the payload[key]
        get_resp = base_endpoint._get("v1/test", json_key="topLevel")
        assert get_resp == {"test": "ok"}

    @patch("requests.request")
    def test_post(self, mocked_request, base_endpoint):
        pass


class TestGeofenceEndpoint:
    pass
