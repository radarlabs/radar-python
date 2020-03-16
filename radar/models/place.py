from .model import Model


class Place(Model):
    """Place of interest
    
    Parameters:
        _id (str)
        name (str)
        chain (dict)
        facebookPlaceId? (str)
        facebookId? (str)
        location (GeoJSON.Point)
        categories (`list` of str)
        metadata (dict)
    """

    OBJECT_NAME = "Place"
    _DISPLAY_ATTRIBUTES = (
        "_id",
        "name",
        "categories",
    )
