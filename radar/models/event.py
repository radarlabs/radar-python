from .model import Model


class Event(Model):
    """An event represents a change in user state. Events can be uniquely referenced by Radar _id.

    Parameters:
        _id (str): The unique ID for the event, provided by Radar. An alphanumeric string.
        createdAt (datetime): The datetime when the event was created.
        live (bool): true if the event was generated for a user and geofence created with your live API key, false if the event was generated for a user and geofence created with your test API key.
        type (str): The type of event. By default, events are generated when a user enters a geofence (type user.entered_geofence) or exits a geofence (type user.exited_geofence). When Insights is enabled, events will also be generated when a user enters their home (type user.entered_home), exits their home (type user.exited_home), enters their office (type user.entered_office), exits their office (type user.exited_office), starts traveling (type user.started_traveling), or stops traveling (user.stopped_traveling).
        user (dict): The user for which the event was generated.
        geofence (dict): For user.entered_geofence and user.exited_geofence events, the geofence for which the event was generated, including description, tag, and externalId.
        place (dict): For user.entered_place and user.exited_place events, the place for which the event was generated, including name, categories, chain, and facebookId.
        alternatePlaces (list): For user.entered_place events, alternate place candidates.
        verifiedPlace (dict): For verified user.entered_place events, the verified place.
        location (GeoJSON): The location of the user at the time of the event. A Point in GeoJSON format.
        locationAccuracy (float): The accuracy of the user's location at the time of the event in meters.
        confidence (int): The confidence level of the event, one of 3 (high), 2 (medium), or 1 (low).
        duration (float): The duration between entry and exit events, in minutes, for user.exited_geofence and user.exited_place events.
        verification (int): The verification for the event, one of 1 (accepted), -1 (rejected), or 0 (unverified).
    """

    OBJECT_NAME = "Event"
    _DISPLAY_ATTRIBUTES = ("_id", "type", "createdAt")

    def verify(self, verification=None, value=None, verifiedPlaceId=None):
        return self._radar.events.verify(
            id=self._id,
            verification=verification,
            value=value,
            verifiedPlaceId=verifiedPlaceId,
        )

    def delete(self):
        return self._radar.events.delete(id=self._id)
