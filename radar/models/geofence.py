from .model import Model


class Geofence(Model):
    """A geofence represents a custom region or place monitored in your project. Geofences can be uniquely referenced by Radar _id or by tag and externalId.
    
    Parameters:
        _id (string): The unique ID for the geofence, provided by Radar. An alphanumeric string.
        createdAt (datetime): The datetime when the geofence was created.
        live (boolean): true if the geofence was created with your live API key, false if the user was created with your test API key.
        tag (string): An optional group for the geofence.
        externalId (string): An optional external ID for the geofence that maps to your internal database.
        description (string): A description for the geofence.
        type (string): The type of geofence geometry, either polygon or circle.
        geometry (GeoJSON): The geometry of the geofence. Coordinates for type polygon. A calculated polygon approximation for type circle. A Polygon in GeoJSON format.
        geometryCenter (GeoJSON): The center of the circle for type circle. The calculated centroid of the polygon for type polygon. A Point in GeoJSON format.
        geometryRadius (number): The radius of the circle in meters for type circle.
        metadata (dictionary): An optional set of custom key-value pairs for the geofence.
        userId (string): An optional user restriction for the geofence. If set, the geofence will only generate events for the specified user. If not set, the geofence will generate events for all users.
        enabled (boolean): If true, the geofence will generate events. If false, the geofence will not generate events. Defaults to true.
    """

    OBJECT_NAME = "geofence"
    _DISPLAY_ATTRIBUTES = (
        "_id",
        "externalId",
        "tag",
        "description",
    )

    def delete(self):
        return self._radar.geofences.delete(id=self._id)
