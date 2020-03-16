from .api import ApiRequester


class RadarClient:
    """The RadarClient class provides convenient access to Radar's API.

    API endpoints with authentication level Publishable are safe to call client-side.
    You should use your publishable API keys to call these endpoints. Use your Test
    Publishable key for testing and non-production environments. Use your Live
    Publishable key for production environments.

    API endpoints with authentication level Secret are only safe to call server-side.
    You should use your secret API keys to call these endpoints. Use your Test Secret
    key for testing and non-production environments. Use your Live Secret key for
    production environments. Include your API key in the Authorization header.

    Examples:
        >>> from radar import RadarClient
        >>> radar = RadarClient(secret_key="sk_test_123")
        >>> radar.geofences.list()
    """

    def __init__(self, secret_key=None, pub_key=None):
        """Initialize a RadarClient instance with API keys.

        API endpoints with authentication level Secret are only safe to call
        server-side. API endpoints with authentication level Publishable are safe to
        call client-side.

        Args:
            secret_key (str, optional (default=None)): project secret key.
            pub_key (str, optional (default=None)): project publishable key.
        """
        BASE_URL = "https://api.radar.io/"
        self.api_requester = ApiRequester(BASE_URL, secret_key, pub_key)

        # Endpoints
        self._geofences = None
        self._events = None
        self._users = None
        self._context = None
        self._geocode = None
        self._search = None
        self._route = None

    @property
    def geofences(self):
        if self._geofences is None:
            from .endpoints import Geofences

            self._geofences = Geofences(self, self.api_requester)
        return self._geofences

    @property
    def events(self):
        if self._events is None:
            from .endpoints import Events

            self._events = Events(self, self.api_requester)
        return self._events

    @property
    def users(self):
        if self._users is None:
            from .endpoints import Users

            self._users = Users(self, self.api_requester)
        return self._users

    @property
    def context(self):
        if self._context is None:
            from .endpoints import Context

            self._context = Context(self, self.api_requester)
        return self._context

    @property
    def geocode(self):
        if self._geocode is None:
            from .endpoints import Geocode

            self._geocode = Geocode(self, self.api_requester)
        return self._geocode

    @property
    def search(self):
        if self._search is None:
            from .endpoints import Search

            self._search = Search(self, self.api_requester)
        return self._search

    @property
    def route(self):
        if self._route is None:
            from .endpoints import Route

            self._route = Route(self, self.api_requester)
        return self._route
