from unittest.mock import patch, Mock

import pytest

from radar.models.context import RadarContext
from radar.models.geofence import Geofence
from radar.models.region import Region
from radar.models.place import Place


def test_context_model(radar, context_json):
    context = RadarContext(radar, context_json)
    assert context.live == context_json["live"]
    assert len(context.geofences) == 2
    assert type(context.geofences[0]) is Geofence
    assert type(context.geofences[1]) is Geofence

    assert type(context.country) is Region
    assert type(context.state) is Region
    assert type(context.dma) is Region
    assert type(context.postalCode) is Region

    assert context.country.type == "country"
    assert context.state.type == "state"
    assert context.dma.type == "dma"
    assert context.postalCode.type == "postalCode"
