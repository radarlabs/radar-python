from .model import Model
from radar.models.geofence import Geofence
from radar.models.region import Region
from radar.models.place import Place


class RadarContext(Model):
    """Location context
    
    Parameters:
        live (bool)
        geofences (`list` of :class:`~radar.models.geofence.Geofence`)
        place (`list` of :class:`~radar.models.place.Place`, optional)
        country (:class:`~radar.models.region.Region`, optional)
        state (:class:`~radar.models.region.Region`, optional)
        dma (:class:`~radar.models.region.Region`, optional)
        postalCode (:class:`~radar.models.region.Region`, optional)
        fraud (FraudObject, optional)
    """

    OBJECT_NAME = "Context"
    _DISPLAY_ATTRIBUTES = (
        "live",
        "geofences",
        "place",
        "country",
        "state",
        "dma",
        "postalCode",
    )

    def __init__(self, radar, data={}):
        """Initialize a Radar Model instance

        Args:
            radar (:class:`~radar.RadarClient`): RadarClient for instance CRUD actions
            raw_json (dict): raw data to initialize the model with
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
            elif attribute in ["country", "state", "dma", "postalCode"]:
                region = Region(radar, data[attribute])
                setattr(self, attribute, region)
            else:
                setattr(self, attribute, value)
