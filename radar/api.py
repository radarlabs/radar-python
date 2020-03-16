import platform
import requests

from . import errors

try:
    import pkg_resources

    __version__ = pkg_resources.get_distribution("radar").version
except Exception:
    __version__ = "unknown"

# TODO: add remaining error codes
ERROR_LOOKUP = {
    400: errors.InvalidRequestError,
    401: errors.AuthenticationError,
    402: errors.PaymentRequiredError,
    403: errors.ForbiddenError,
    404: errors.NotFoundError,
    429: errors.RateLimitError,
    500: errors.InternalServerError,
}


class ApiRequester(object):
    """Api requesting object"""

    def __init__(self, base_url, secret_key, pub_key=None):
        """Initializes API requester class with api keys.

        Args:
            base_url (str): URL of radar api
            secret_key (str): api key for secret authentication
            pub_key (str, optional (default=None)): api key for publishable authentication.

        https://radar.io/documentation/api#auth
        """
        self.BASE_URL = base_url
        self.secret_key = secret_key
        self.pub_key = pub_key

    def _request(self, method, path, params=None, data=None, auth_type="secret_key"):
        """Makes the api request with headers and error handling

        Args:
            method (str): HTTP method to use (e.g., GET, POST, PUT, DELETE)
            path (str): Formatted path to api resource
            params (dict, optional (default=None)): query params to append to url.
            data (dict, optional (default=None)): body to attach to request.
            auth_type (str, optional (default="secret key")): auth type required for the request.

        Returns:
            dict: json of the request's response
        """
        headers = self._get_headers(auth_type)
        url = self.BASE_URL + path
        response = requests.request(
            method, url, params=params, data=data, headers=headers,
        )
        if response.status_code >= 200 and response.status_code < 300:
            return response.json()
        return self.handle_error_codes(response)

    def _get_headers(self, auth_type):
        """Generates request headers needed for api calls.

        Args:
            auth_type (str, optional (default="secret_key")): authorization type, "secret_key" or "pub_key".

        Returns:
            dict: dictionary of headers to include
        """
        api_key = self.secret_key if (auth_type == "secret_key") else self.pub_key
        if api_key is None:
            error_message = f"RadarClient is missing api key: {auth_type}"
            raise errors.RadarError(error_message)
        user_agent = "radar-python/{} (Python {})".format(
            __version__, platform.python_version(),
        )

        # TODO(coryp): determine header fields we want - user agent, lib versions
        headers = {
            "Authorization": api_key,
            "User-Agent": user_agent,
        }
        return headers

    def handle_error_codes(self, response):
        """Raises respective exception for a given error status code."""
        status_code = response.status_code
        reason = response.reason
        if status_code in ERROR_LOOKUP:
            api_error = ERROR_LOOKUP[status_code]
            raise api_error(reason, status_code)

        # let requests raise error if not a Radar Error
        response.raise_for_status()
