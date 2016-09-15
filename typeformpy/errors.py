class ClientError(StandardError):
    def __init__(self):
        pass

    def __new__(cls, *args):
        pass


class ServerError(StandardError):
    def __init__(self):
        pass

    def __new__(cls, *args):
        pass


class BadRequest(StandardError):
    def __init__(self):
        pass

    def __new__(cls, *args):
        pass


class UnauthorizedAccess(StandardError):
    def __init__(self):
        pass

    def __new__(cls, *args):
        pass


class NotFound(StandardError):
    def __init__(self):
        pass

    def __new__(cls, *args):
        pass


class Unavailable(StandardError):
    def __init__(self):
        pass

    def __new__(cls, *args):
        pass
