from .model import Model
from radar.models.geofence import Geofence
from radar.models.place import Place


class User(Model):
    """A user represents a user tracked in your project. Users can be referenced by Radar _id, userId, or deviceId.

    Parameters:
        _id (string): A unique ID for the user, provided by Radar. An alphanumeric string.
        live (boolean): true if the user was created with your live API key, false if the user was created with your test API key.
        userId (string): A stable unique ID for the user.
        deviceId (string): A device ID for the user.
        description (string): An optional description for the user.
        metadata (dict): An optional dictionary of custom metadata for the user.
        location (GeoJSON): The user's last known location, a Point in GeoJSON format.
        locationAccuracy (number): The accuracy of the user's last known location in meters.
        foreground (boolean): true if the user's last known location was updated in the foreground, false if the user's last known location was updated in the background.
        stopped (boolean): true if the user's last known location was updated while stopped, false if the user's last known location was updated while moving.
        deviceType (string): The user's device type, one of iOS, Android, or Web.
        updatedAt (datetime): The datetime when the user's location was last updated.
        geofences (`list` of :class:`~radar.models.geofence.Geofence`): An array of the user's last known geofences.
        place (:class:`~radar.models.place.Place`): When Places is enabled, the user's last known place.
        insights (dict): When Insights is enabled, the user's learned approximate home and office locations, and home, office, and traveling state.
    """

    OBJECT_NAME = "User"
    _DISPLAY_ATTRIBUTES = ("userId", "_id", "deviceId")

    def __init__(self, radar, data={}):
        """Initialize a Radar Model instance

        Args:
            radar (RadarClient): RadarClient for instance CRUD actions
            data (dict): raw data to initialize the model with
        """
        self._radar = radar
        self.raw_json = data
        for attribute, value in data.items():
            if attribute == "geofences":
                geofences = [Geofence(radar, geofence) for geofence in data[attribute]]
                setattr(self, attribute, geofences)
            elif attribute == "place":
                place = Place(radar, data[attribute])
                setattr(self, attribute, place)
            else:
                setattr(self, attribute, value)

    def delete(self):
        return self._radar.users.delete(id=self._id)
