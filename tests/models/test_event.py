from unittest.mock import patch, Mock

import pytest

from radar.models.event import Event
from radar.api import ApiRequester


def test_event_model(radar, event_json):
    event = Event(radar, event_json)
    assert event._id == event_json["_id"]
    assert event.type == event_json["type"]
    assert event.live == event_json["live"]
    assert event.createdAt == event_json["createdAt"]
    assert event.confidence == event_json["confidence"]
    assert event.user == event_json["user"]


@patch.object(ApiRequester, "_request")
def test_event_delete(mock_request, radar, event_json):
    event = Event(radar, event_json)
    event.delete()
    path = f"v1/events/{event._id}"
    mock_request.assert_called_once_with("DELETE", path)
