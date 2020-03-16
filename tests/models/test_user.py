from unittest.mock import patch, Mock

import pytest

from radar.models.user import User
from radar.models.geofence import Geofence
from radar.api import ApiRequester


def test_user_model(radar, user_json):
    user = User(radar, user_json)
    assert user._id == user_json["_id"]
    assert user.live == user_json["live"]
    assert user.updatedAt == user_json["updatedAt"]
    assert user.createdAt == user_json["createdAt"]
    assert len(user.geofences) == 2
    assert type(user.geofences[0]) is Geofence
    assert type(user.geofences[1]) is Geofence
    assert user.userId == user_json["userId"]


@patch.object(ApiRequester, "_request")
def test_user_delete(mock_request, radar, user_json):
    user = User(radar, user_json)
    user.delete()
    path = f"v1/users/{user._id}"
    mock_request.assert_called_once_with("DELETE", path)
