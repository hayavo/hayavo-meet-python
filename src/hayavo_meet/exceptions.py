class HayavoMeetError(Exception):
    pass


class AuthenticationError(HayavoMeetError):
    pass


class APIRequestError(HayavoMeetError):
    pass


class ValidationError(HayavoMeetError):
    pass