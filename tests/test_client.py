import pytest
from unittest.mock import patch, Mock

from radar import RadarClient, endpoints
from radar.api import ApiRequester
from radar.errors import RadarError


def test_radar_client_initialized(radar):
    assert type(radar.api_requester) is ApiRequester
    assert radar.api_requester.BASE_URL == "https://api.radar.io/"
    assert type(radar.geofences) is endpoints.Geofences
    assert type(radar.events) is endpoints.Events
    assert type(radar.users) is endpoints.Users
    assert type(radar.events) is endpoints.Events
    assert type(radar.context) is endpoints.Context


def test_init_with_secret_key():
    radar = RadarClient("sk123")
    assert radar.api_requester.secret_key == "sk123"
    assert radar.api_requester.pub_key is None


def test_init_with_pub_key():
    radar = RadarClient(pub_key="pubkey123")
    assert radar.api_requester.pub_key == "pubkey123"
    assert radar.api_requester.secret_key is None


def test_init_with_all_keys():
    radar = RadarClient(secret_key="sk123", pub_key="pubkey123")
    assert radar.api_requester.pub_key == "pubkey123"
    assert radar.api_requester.secret_key == "sk123"


@patch("requests.request")
def test_missing_secret_key(mocked_request):
    mocked_request.return_value = Mock(status_code=200)
    radar = RadarClient(pub_key="pubkey123")
    with pytest.raises(RadarError) as err:
        raw_json = radar.api_requester._request("GET", "/test")
    assert "RadarClient is missing api key: secret_key" in str(err.value)


@patch("requests.request")
def test_missing_pub_key(mocked_request):
    mocked_request.return_value = Mock(status_code=200)
    radar = RadarClient(secret_key="123")
    with pytest.raises(RadarError) as err:
        raw_json = radar.api_requester._request("GET", "/test", auth_type="pub_key")
    assert "RadarClient is missing api key: pub_key" in str(err.value)
