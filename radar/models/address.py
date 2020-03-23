from .model import Model


class Address(Model):
    """Location address

    Parameters:
        borough (str)
        city (str)
        confidence (str): one of 'exact', 'interpolated', 'fallback'
        country (str)
        countryCode (str)
        countryFlag (str)
        distance (float)
        formattedAddress (str)
        geometry (GeoJSON.Point)
        addressLabel (str)
        placeLabel (str)
        number (str)
        latitude (float)
        longitude (float)
        neighborhood (str)
        postalCode (str)
        source (str)
        state (str)
        stateCode (str)
        street (str)
    """

    OBJECT_NAME = "Address"
    _DISPLAY_ATTRIBUTES = (
        "latitude",
        "longitude",
        "formattedAddress",
        "placeLabel",
    )
