import os
import json

import pytest

from radar import RadarClient

MOCK_DATA_PATH = "tests/mock_data/{file_name}"


class TestHelpers:
    def load_mock_data(file_name):
        json_path = MOCK_DATA_PATH.format(file_name=file_name)
        with open(json_path) as f:
            return json.load(f)


@pytest.fixture(scope="module")
def radar():
    radar = RadarClient(secret_key="sk_test_123", pub_key="pk_test_123")
    return radar


@pytest.fixture(scope="module")
def geofence_json():
    return TestHelpers.load_mock_data("geofence.json")


@pytest.fixture(scope="module")
def user_json():
    return TestHelpers.load_mock_data("user.json")


@pytest.fixture(scope="module")
def event_json():
    return TestHelpers.load_mock_data("event.json")


@pytest.fixture(scope="module")
def context_json():
    return TestHelpers.load_mock_data("context.json")
