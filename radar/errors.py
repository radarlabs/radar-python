# place holders


class RadarError(Exception):
    """Base class to define Radar API errors

    https://radar.io/documentation/api#errors
    """

    def __init__(self, message=None, status_code=None, response_body=None):
        Exception.__init__(self, message)

        self.message = message
        self.status_code = status_code
        self.response_body = response_body

    def __str__(self):
        if self.status_code is not None:
            return "{0}: {1}".format(self.status_code, self.message)
        else:
            return "{0}".format(self.message)


class InvalidRequestError(RadarError):
    pass


class AuthenticationError(RadarError):
    pass


class PaymentRequiredError(RadarError):
    pass


class ForbiddenError(RadarError):
    pass


class NotFoundError(RadarError):
    pass


class RateLimitError(RadarError):
    pass


class APIError(RadarError):
    pass


class InternalServerError(RadarError):
    pass
