class TypeFormError(StandardError):
    def __init__(self, error):
        self.__init__("The Typeform API returned the following error: {}"
                      .format(error))

    def __new__(cls, *args):
        pass


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
