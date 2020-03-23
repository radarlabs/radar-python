from .model import Model


class RouteDistance:
    """Travel distance of the route
    
    Parameters:
        value (str): value of distance in requested units
        text (str): human readable distance
    """

    def __init__(self, value, text):
        self.value = value
        self.text = text

    def __repr__(self):
        return f"<text={self.text} value={self.value}>"

    def to_feet(self):
        pass


class RouteDuration:
    """Travel duration of the route
    
    Parameters:
        value (str): minutes
        text (str): human readable duration
    """

    def __init__(self, value, text):
        self.value = value
        self.text = text

    def __repr__(self):
        return f"<text={self.text} value={self.value}>"

    def to_sec(self):
        pass


class Route:
    """The travel distance and duration between two locations

    Parameters:
        mode (str): one of 'car', 'bike', 'foot', 'transit'
        duration (:class:`~radar.models.route.RouteDuration`)
        distance (:class:`~radar.models.route.RouteDistance`)
    """

    def __init__(self, distance=None, duration=None, mode=None):
        self.mode = mode

        if distance:
            self.distance = RouteDuration(
                value=distance.get("value"), text=distance.get("text")
            )
        else:
            self.distance = None

        if duration:
            self.duration = RouteDuration(
                value=duration.get("value"), text=duration.get("text")
            )
        else:
            self.duration = None

    def __repr__(self):
        fields = []
        if self.distance:
            fields.append(f"distance={self.distance.text}")
        if self.duration:
            fields.append(f"duration={self.duration.text}")
        display_str = f"<{' '.join(fields)}>"
        return display_str


class Routes(Model):
    """A collection of :class:`~radar.models.route.Route`"""

    OBJECT_NAME = "Routes"
    _DISPLAY_ATTRIBUTES = (
        "geodesic",
        "transit",
        "car",
        "bike",
        "foot",
    )

    def __init__(self, radar, data={}):
        """Initialize a Radar Routes instance

        Args:
            radar (RadarClient): RadarClient for instance CRUD actions
            data (dict): raw data to initialize the model with
        """
        self._radar = radar
        self.raw_json = data
        for attribute, value in data.items():
            if attribute in ["geodesic", "transit", "car", "bike", "foot"]:
                route = Route(
                    distance=value.get("distance"),
                    duration=value.get("duration"),
                    mode=attribute,
                )
                setattr(self, attribute, route)
            else:
                setattr(self, attribute, value)
