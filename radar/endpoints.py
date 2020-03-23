from radar.models.geofence import Geofence
from radar.models.user import User
from radar.models.event import Event
from radar.models.context import RadarContext
from radar.models.address import Address
from radar.models.region import Regions
from radar.models.place import Place
from radar.models.route import Routes

from radar.errors import RadarError
from radar.utils import remove_none_values

GEOFENCE_PATH = {
    "geofences": "v1/geofences",
    "geofence_id": "v1/geofences/{id}",
    "geofence_tag": "v1/geofences/{tag}/{externalId}",
    "geofence_id_users": "v1/geofences/{id}/users",
    "geofence_tag_users": "v1/geofences/{tag}/{externalId}/users",
    "users": "v1/users",
    "user_id": "v1/users/{id}",
    "events": "v1/events",
    "event_id": "v1/events/{id}",
    "event_verification": "v1/events/{id}/verification",
    "context": "v1/context",
}

USER_PATH = {
    "users": "v1/users",
    "user_id": "v1/users/{id}",
}

EVENT_PATH = {
    "events": "v1/events",
    "event_id": "v1/events/{id}",
    "event_verification": "v1/events/{id}/verification",
}

CONTEXT_PATH = {
    "context": "v1/context",
}

GEOCODE_PATH = {
    "geocode_forward": "v1/geocode/forward",
    "geocode_reverse": "v1/geocode/reverse",
    "geocode_ip": "v1/geocode/ip",
}

SEARCH_PATH = {
    "search_users": "v1/search/users",
    "search_geofences": "v1/search/geofences",
    "search_places": "v1/search/places",
    "search_autocomplete": "v1/search/autocomplete",
}

ROUTE_PATH = {
    "route_distance": "v1/route/distance",
}

API_PATH = {
    **GEOFENCE_PATH,
    **USER_PATH,
    **EVENT_PATH,
    **CONTEXT_PATH,
    **GEOCODE_PATH,
    **SEARCH_PATH,
    **ROUTE_PATH,
}


class _Endpoint:
    """Base class defining a Radar API Endpoint

    get, put, post, delete methods call the api requester, and return json
    """

    def __init__(self, radar, requester):
        self._radar = radar
        self.requester = requester

    def _get(self, path, params=None, json_key=None, auth_type="secret_key"):
        raw_json = self.requester._request(
            "GET", path, params=params, auth_type=auth_type
        )
        return raw_json.get(json_key, raw_json)

    def _post(self, path, data, json_key=None):
        raw_json = self.requester._request("POST", path, data=data)
        return raw_json.get(json_key, raw_json)

    def _put(self, path, data, json_key=None):
        raw_json = self.requester._request("PUT", path, data=data)
        return raw_json.get(json_key, raw_json)

    def _delete(self, path):
        raw_json = self.requester._request("DELETE", path)
        return raw_json


class Geofences(_Endpoint):
    endpoint = "geofences"
    REQUIRED_KEYS = set(["description", "type", "coordinates"])

    def list(self, limit=None, createdBefore=None, createdAfter=None, tag=None):
        """Lists geofences. Geofences are sorted descending by createdAt

        https://radar.io/documentation/api#list-geofences

        Args:
            limit (int, optional (default=100)): max number of geofences to return.
            createdBefore (datetime, optional (default=None)): pagination cursor.
            createdAfter (datetime, optional (default=None)): pagination cursor.
            tag (str, optional (default=None)): lists geofences with specified tag.

        Returns:
            `list` of :class:`~radar.models.geofence.Geofence`
        """
        path = API_PATH["geofences"]
        params = {
            "limit": limit,
            "tag": tag,
            "createdBefore": createdBefore,
            "createdAfter": createdAfter,
        }
        query_params = remove_none_values(params)

        raw_geofences = self._get(path, params=query_params, json_key="geofences")
        return [Geofence(self._radar, data) for data in raw_geofences]

    def get(self, id=None, tag=None, externalId=None):
        """Gets a geofence by id or tag and externalId

        https://radar.io/documentation/api#get-geofence

        Returns:
            :class:`~radar.models.geofence.Geofence`
        """
        if id is not None:
            path = API_PATH["geofence_id"].format(id=id)
        else:
            # check tag and externalId provided
            path = API_PATH["geofence_tag"].format(tag=tag, externalId=externalId)

        raw_geofence = self._get(path, json_key="geofence")
        return Geofence(self._radar, raw_geofence)

    def list_users(
        self,
        id=None,
        tag=None,
        externalId=None,
        limit=None,
        updateBefore=None,
        updatedAfter=None,
    ):
        """Lists users in a geofence. 

        The geofence can be uniquely referenced by Radar _id or by tag and externalId. 
        Users are sorted descending by updatedAt.

        https://radar.io/documentation/api#list-geofence-users

        Returns:
            `list` of :class:`~radar.models.user.User`
        """
        if id is not None:
            path = API_PATH["geofence_id_users"].format(id=id)
        else:
            path = API_PATH["geofence_tag_users"].format(tag=tag, externalId=externalId)

        params = {
            "limit": limit,
            "updateBefore": updateBefore,
            "updatedAfter": updatedAfter,
        }
        query_params = remove_none_values(params)

        raw_users = self._get(path, params=query_params, json_key="users")
        return [User(self._radar, data) for data in raw_users]

    def create(self, data={}):
        """Creates a geofence.

        If a geofence with the specified tag and externalId already exists, the request
        will fail.

        https://radar.io/documentation/api#create-geofence
        
        Returns:
            :class:`~radar.models.geofence.Geofence`
        """
        self._check_required_keys_exist(data)
        path = API_PATH["geofences"]

        raw_geofence = self._post(path, data=data, json_key="geofence")
        return Geofence(self._radar, raw_geofence)

    def upsert(self, tag=None, externalId=None, data={}):
        """Upserts a geofence.

        If a geofence with the specified tag and externalId already exists, it will be
        updated. If not, it will be created.

        https://radar.io/documentation/api#upsert-geofence
        
        Returns:
            :class:`~radar.models.geofence.Geofence`
        """
        self._check_required_keys_exist(data)
        path = API_PATH["geofence_tag"].format(tag=tag, externalId=externalId)

        raw_geofence = self._put(path, data=data, json_key="geofence")
        return Geofence(self._radar, raw_geofence)

    def delete(self, id=None, tag=None, externalId=None):
        """https://radar.io/documentation/api#delete-geofence"""
        if id is not None:
            path = API_PATH["geofence_id"].format(id=id)
        else:
            # check tag and externalId provided
            path = API_PATH["geofence_tag"].format(tag=tag, externalId=externalId)

        raw_json = self._delete(path)
        return raw_json

    def _check_required_keys_exist(self, data):
        missing_keys = self.REQUIRED_KEYS - data.keys()
        if missing_keys:
            raise RadarError(message=f"Missing fields: {missing_keys}")
        return


class Users(_Endpoint):
    endpoint = "users"

    def list(self, limit=None, updatedBefore=None, updatedAfter=None):
        """List users, sorted descending by updatedAt

        https://radar.io/documentation/api#list-users

        Args:
            limit (int, optional (default=100)): Max number of users to return.
            updateBefore (datetime, optional): A cursor for use in pagination. 
                Retrieves users updated before the specified datetime.
            updatedAfter (datetime, optional): A cursor for use in pagination. 
                Retrieves users updated after the specified datetime.

        Returns:
            `list` of :class:`~radar.models.user.User`
        """
        path = API_PATH["users"]
        params = {
            "limit": limit,
            "updatedBefore": updatedBefore,
            "updatedAfter": updatedAfter,
        }
        query_params = remove_none_values(params)

        raw_users = self._get(path, params=query_params, json_key="users")
        return [User(self._radar, data) for data in raw_users]

    def get(self, id=None, userId=None, deviceId=None):
        """Gets a user. The user can be referenced by Radar _id, userId, or deviceId

        https://radar.io/documentation/api#get-user

        Returns:
            :class:`~radar.models.user.User`
        """
        user_id = id or userId or deviceId
        path = API_PATH["user_id"].format(id=user_id)

        raw_user = self._get(path, json_key="user")
        return User(self._radar, raw_user)

    def delete(self, id=None, userId=None, deviceId=None):
        """Deletes a user. The user can be referenced by Radar _id, userId, or deviceId

        https://radar.io/documentation/api#delete-user
        """
        user_id = id or userId or deviceId
        path = API_PATH["user_id"].format(id=user_id)

        raw_json = self._delete(path)
        return raw_json


class Events(_Endpoint):
    endpoint = "events"

    def list(self, limit=None, createdBefore=None, createdAfter=None):
        """Lists events. Events are sorted descending by createdAt.

        https://radar.io/documentation/api#list-events
        
        Args:
            limit (int, optional (default=100)): Max number of events to return.
            createdBefore (datetime, optional): A cursor for use in pagination. 
                Retrieves events created before the specified datetime.
            createdAfter (datetime, optional): A cursor for use in pagination. 
                Retrieves events created after the specified datetime.

        Returns:
            `list` of :class:`~radar.models.event.Event`
        """
        path = API_PATH["events"]
        params = {
            "limit": limit,
            "createdBefore": createdBefore,
            "createdAfter": createdAfter,
        }
        query_params = remove_none_values(params)

        raw_events = self._get(path, params=query_params, json_key="events")
        return [Event(self._radar, data) for data in raw_events]

    def get(self, id):
        """Gets an event. The event can be uniquely referenced by Radar _id
        
        https://radar.io/documentation/api#get-event


        Returns:
            :class:`~radar.models.event.Event`
        """
        path = API_PATH["event_id"].format(id=id)

        raw_event = self._get(path, json_key="event")
        return Event(self._radar, raw_event)

    def verify(self, id, verification=None, value=None, verifiedPlaceId=None):
        """Verifies an event. 
        
        Events can be accepted or rejected after user check-ins or other forms of verification.
        Event verifications will be used to improve the confidence level of future events.

        https://radar.io/documentation/api#verify-event

        Args:
            id (str): id of the event to verify
            verification (str, optional): one of "accept", "reject", "unverify"
            value (int, optional): one of 1 (accept), -1 (reject), 0 (unverify)
            verifiedPlaceId (str, optional): For user.entered_place events, the ID of the verified place.
        
        Example:
            >>> radar.events.verify('123', 'accept')
            >>> radar.events.verify('123', value=1)
        """
        if value:
            if value not in [-1, 0, 1]:
                raise RadarError(
                    message="value must be one of 1 (accept), -1 (reject), 0 (unverify)"
                )
        else:
            verification_options = {"accept": 1, "reject": -1, "unverify": 0}
            if verification not in verification_options:
                raise RadarError(
                    message="verification must be one of 'accept', 'reject', 'unverify'"
                )
            verify_value = verification_options[verification]

        path = API_PATH["event_verification"].format(id=id)
        data = {
            "verification": verify_value,
            "verifiedPlaceId": verifiedPlaceId,
        }
        data = remove_none_values(data)

        raw_json = self._put(path, data=data)
        return raw_json

    def delete(self, id):
        """Deletes an event. The event can be uniquely referenced by Radar _id

        https://radar.io/documentation/api#delete-event
        """
        path = API_PATH["event_id"].format(id=id)

        raw_json = self._delete(path)
        return raw_json


class Context(_Endpoint):
    endpoint = "context"

    def get(self, coordinates):
        """Gets context for a location without sending device or user identifiers to the server.

        Args:
            coordinates ((latitude, longitude)): the coordinates of the location
        
        Examples:
            >>> radar.context.get(coordinates=(40.123, -73.456))

        Returns:
            :class:`~radar.models.context.RadarContext`: object with the radar context for the provided location
        """
        if coordinates:
            (latitude, longitude) = coordinates
        if latitude is None or longitude is None:
            raise RadarError(message="Coordinates as (latitude,longitude) are required")

        path = API_PATH["context"]
        params = {"coordinates": f"{latitude},{longitude}"}

        raw_context = self._get(
            path, params=params, json_key="context", auth_type="pub_key"
        )
        return RadarContext(self._radar, raw_context)


class Geocode(_Endpoint):
    endpoint = "geocode"

    def forward(self, query):
        """Geocodes an address, converting address to coordinates.
        
        https://radar.io/documentation/api#geocode-forward

        Args:
            query (str): The address to geocode.
        
        Returns:
            `list` of :class:`~radar.models.address.Address`
        """
        path = API_PATH["geocode_forward"]
        params = {"query": query}

        raw_addresses = self._get(path, params=params, json_key="addresses")
        # TODO move to single address if this changes?
        return [Address(self._radar, data) for data in raw_addresses]

    def reverse(self, coordinates):
        """Reverse geocodes a location, converting coordinates to address.
        
        https://radar.io/documentation/api#geocode-reverse

        Args:
            coordinates ((latitude, longitude)): the coordinates to reverse geocode

        Returns:
            `list` of :class:`~radar.models.address.Address`
        """
        if coordinates:
            (latitude, longitude) = coordinates
        if latitude is None or longitude is None:
            raise RadarError(message="Coordinates as (latitude,longitude) are required")

        path = API_PATH["geocode_reverse"]
        params = {"coordinates": f"{latitude},{longitude}"}

        raw_addresses = self._get(path, params=params, json_key="addresses")
        # TODO move to single address if this changes?
        return [Address(self._radar, data) for data in raw_addresses]

    def ip(self, ip):
        """Geocodes an IP address, converting IP address to partial address.
        
        https://radar.io/documentation/api#geocode-ip

        Args:
            ip (str):  The IP address to geocode.
        
        Returns:
            `:class:`~radar.models.address.Address`
        """
        path = API_PATH["geocode_ip"]
        params = {"ip": ip}

        raw_address = self._get(path, params=params, json_key="address")
        return Address(self._radar, raw_address)


class Search(_Endpoint):
    endpoint = "search"

    def users(self, near, radius=None, limit=None):
        """Searches for users near a location, sorted by distance.
        
        https://radar.io/documentation/api#search-users

        Args:
            near ((latitude, longitude)): A location for the search. pair of latitude,longitude.
            radius (int, optional (default=1000)): The radius to search, in meters. A number between 100 and 10000.
            limit (int, optional (default=100)): The max number of places to return. A number between 1 and 1000.
        
        Returns:
            `list` of :class:`~radar.models.user.User`
        """
        path = API_PATH["search_users"]
        (latitude, longitude) = near
        params = {"near": f"{latitude},{longitude}", "radius": radius, "limit": limit}
        query_params = remove_none_values(params)

        raw_users = self._get(path, params=query_params, json_key="users")
        return [User(self._radar, data) for data in raw_users]

    def geofences(self, near, tags=None, radius=None, limit=None):
        """Searches for geofences near a location, sorted by distance.

        https://radar.io/documentation/api#search-geofences

        Args:
            near ((latitude, longitude)): A location for the search in the format (latitude,longitude).
            tags (str, optional): The tags to filter. A string, comma-separated.
            radius (int, optional (default=1000)): The radius to search, in meters. A number between 100 and 10000.
            limit (int, optional (default=100)): The max number of geofences to return. A number between 1 and 1000.
        
        Returns:
            `list` of :class:`~radar.models.geofence.Geofence`
        """
        path = API_PATH["search_geofences"]
        (latitude, longitude) = near
        params = {
            "near": f"{latitude},{longitude}",
            "tags": tags,
            "radius": radius,
            "limit": limit,
        }
        query_params = remove_none_values(params)

        raw_geofences = self._get(path, params=query_params, json_key="geofences")
        return [Geofence(self._radar, data) for data in raw_geofences]

    def places(
        self, near, chains=None, categories=None, groups=None, radius=None, limit=None
    ):
        """Searches for places near a location, sorted by distance.
        
        https://radar.io/documentation/api#search-places

        Args:
            near ((latitude,longitude)): A location for the search in the format (latitude,longitude).
            chains (str, optional): The chain slugs to filter. A string, comma-separated.
            categories (str, optional): The categories to filter. A string, comma-separated.
            groups (str, optional): The groups to filter. A string, comma-separated.
            radius (int, optional (default=1000)): The radius to search, in meters. A number between 100 and 10000.
            limit (int, optional (default=100)): The max number of places to return. A number between 1 and 1000.

        Returns:
            `list` of :class:`~radar.models.place.Place`
        
        Example:
            >>> radar.search.places(query="brooklyn roasting", near=(40.7041029,-73.98706))
        """

        path = API_PATH["search_places"]
        (latitude, longitude) = near
        params = {
            "near": f"{latitude},{longitude}",
            "chains": chains,
            "categories": categories,
            "groups": groups,
            "radius": radius,
            "limit": limit,
        }
        query_params = remove_none_values(params)

        raw_places = self._get(path, params=query_params, json_key="places")
        return [Place(self._radar, data) for data in raw_places]

    def autocomplete(self, query, near, limit=None):
        """Autocompletes partial addresses and place names, sorted by relevance.
        
        https://radar.io/documentation/api#search-autocomplete

        Args:
            query (str): The partial address or place name to autocomplete.
            near ((latitude,longitude)): A location for the search in the format (latitude,longitude).
            limit (int, optional (default=10)): The max number of addresses to return. A number between 1 and 100.

        Returns:
            `list` of :class:`~radar.models.address.Address`
        
        Example:
            >>> radar.search.autocomplete(near=(40.7041029,-73.98706), categories="coffee-shop")
            [<Radar Place: name='Brooklyn Roasting Company'>,
             <Radar Place: name='Starbucks'>,
             <Radar Place: name="Dunkin'">]
        """

        path = API_PATH["search_autocomplete"]
        (latitude, longitude) = near
        params = {
            "query": query,
            "near": f"{latitude},{longitude}",
            "limit": limit,
        }
        query_params = remove_none_values(params)

        raw_addresses = self._get(path, params=params, json_key="addresses")
        return [Address(self._radar, data) for data in raw_addresses]


class Route(_Endpoint):
    endpoint = "route"

    def distance(self, origin, destination, modes, units="metric"):
        """Calculates the travel distance and duration between two locations.
        
        https://radar.io/documentation/api#route-distance

        Args:
            origin (str): The origin. A string in the format latitude,longitude.
            destination (str): The destination. A string in the format latitude,longitude.
            modes (str): The travel modes. A string, comma-separated, including one or more of foot, bike, car, and transit.
            units (str, optional (default="metric")): The distance units. A string, metric or imperial.
        
        Returns:
            :class:`~radar.models.route.Routes`
        """
        path = API_PATH["route_distance"]
        (origin_lat, origin_lng) = origin
        (destination_lat, destination_lng) = destination

        UNIT_OPTIONS = ["metric", "imperial"]
        if units not in UNIT_OPTIONS:
            raise RadarError(message="units must be 'metric' or 'imperial'")

        MODE_OPTIONS = ["car", "bike", "transit", "foot"]
        if not all([mode in MODE_OPTIONS for mode in modes.split(",")]):
            raise RadarError(
                message="modes must be comma-separated string including one or more of 'foot,bike,car,transit'"
            )

        query_params = {
            "origin": f"{origin_lat},{origin_lng}",
            "destination": f"{destination_lat},{destination_lng}",
            "modes": modes,
            "units": units,
        }

        raw_routes = self._get(path, params=query_params, json_key="routes")
        return Routes(self._radar, raw_routes)
