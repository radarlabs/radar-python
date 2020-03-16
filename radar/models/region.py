from .model import Model


class Region(Model):
    """A location region, either country, state, dma, or postalCode
    
    Parameters:
        _id (str)
        type (str)
        name (str)
        code (str)
        flag (str)
    """

    OBJECT_NAME = "Region"
    _DISPLAY_ATTRIBUTES = (
        "type",
        "name",
        "code",
    )


class Regions(Model):
    """A collection of :class:`~radar.models.region.Region`"""

    OBJECT_NAME = "Regions"
    _DISPLAY_ATTRIBUTES = (
        "country",
        "state",
        "dma",
        "postalCode",
    )
