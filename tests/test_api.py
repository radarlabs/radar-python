import pytest
from unittest.mock import patch, Mock

from radar.api import ApiRequester
from radar.errors import (
    InvalidRequestError,
    AuthenticationError,
    PaymentRequiredError,
    ForbiddenError,
    NotFoundError,
    InternalServerError,
)


def test_get_headers(radar):
    headers = radar.api_requester._get_headers("secret_key")
    assert "Authorization" in headers
    assert "User-Agent" in headers
    assert headers["Authorization"] == radar.api_requester.secret_key
    assert "radar-python" in headers["User-Agent"]

    headers = radar.api_requester._get_headers("pub_key")
    assert "Authorization" in headers
    assert "User-Agent" in headers
    assert headers["Authorization"] == radar.api_requester.pub_key
    assert "radar-python" in headers["User-Agent"]


@patch("requests.request")
def test_requester_correct_auth_types(mocked_request, radar):
    mocked_request.return_value = Mock(status_code=200)

    # _request() should get 'secret_key' headers by default
    with patch.object(ApiRequester, "_get_headers") as mock_get_headers:
        raw_json = radar.api_requester._request("GET", "/test")
        mock_get_headers.assert_called_once_with("secret_key")

    # _request() should get 'pub_key' headers when auth_type is 'pub_key'
    with patch.object(ApiRequester, "_get_headers") as mock_get_headers:
        raw_json = radar.api_requester._request("GET", "/test", auth_type="pub_key")
        mock_get_headers.assert_called_once_with("pub_key")


@patch("requests.request")
def test_requester_on_success(mocked_request, radar):
    mocked_request.return_value = Mock(
        status_code=200, json=lambda: {"data": {"test": "ok"}}
    )

    raw_json = radar.api_requester._request("GET", "/test")

    assert raw_json["data"]["test"] == "ok"


@patch("requests.request")
def test_requester_raises_400(mocked_request, radar):
    mocked_request.return_value = Mock(status_code=400)

    with pytest.raises(InvalidRequestError) as err:
        raw_json = radar.api_requester._request("GET", "v1/geofences/123456")
    assert "400" in str(err.value)


@patch("requests.request")
def test_requester_raises_401(mocked_request, radar):
    mocked_request.return_value = Mock(status_code=401)

    with pytest.raises(AuthenticationError) as err:
        raw_json = radar.api_requester._request("GET", "v1/geofences/123456")
    assert "401" in str(err.value)


@patch("requests.request")
def test_requester_raises_402(mocked_request, radar):
    mocked_request.return_value = Mock(status_code=402)

    with pytest.raises(PaymentRequiredError) as err:
        raw_json = radar.api_requester._request("GET", "v1/geofences/123456")
    assert "402" in str(err.value)


@patch("requests.request")
def test_requester_raises_403(mocked_request, radar):
    mocked_request.return_value = Mock(status_code=403)

    with pytest.raises(ForbiddenError) as err:
        raw_json = radar.api_requester._request("GET", "v1/geofences/123456")
    assert "403" in str(err.value)


@patch("requests.request")
def test_requester_raises_404(mocked_request, radar):
    mocked_request.return_value = Mock(status_code=404)

    with pytest.raises(NotFoundError) as err:
        raw_json = radar.api_requester._request("GET", "v1/geofences/123456")
    assert "404" in str(err.value)


@patch("requests.request")
def test_requester_raises_500(mocked_request, radar):
    mocked_request.return_value = Mock(status_code=500)

    with pytest.raises(InternalServerError) as err:
        raw_json = radar.api_requester._request("GET", "v1/geofences/123456")
    assert "500" in str(err.value)
