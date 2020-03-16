from unittest.mock import patch, Mock

import pytest

from radar.models.geofence import Geofence
from radar.api import ApiRequester


def test_geofence_model(radar, geofence_json):
    geofence = Geofence(radar, geofence_json)
    assert geofence._id == geofence_json["_id"]
    assert geofence.description == geofence_json["description"]
    assert geofence.live == geofence_json["live"]
    assert geofence.tag == geofence_json["tag"]
    assert geofence.externalId == geofence_json["externalId"]
    assert geofence.createdAt == geofence_json["createdAt"]
    assert geofence.updatedAt == geofence_json["updatedAt"]


@patch.object(ApiRequester, "_request")
def test_geofence_delete(mock_request, radar, geofence_json):
    geofence = Geofence(radar, geofence_json)
    geofence.delete()
    path = f"v1/geofences/{geofence._id}"
    mock_request.assert_called_once_with("DELETE", path)
