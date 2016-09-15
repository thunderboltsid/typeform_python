import requests
from errors import TypeFormError, ClientError, ServerError, BadRequest, \
    UnauthorizedAccess, NotFound, Unavailable


_VERSION = "0.0.2"
_HEADERS = {
    "User-Agent": "typeform-rest-{}".format(_VERSION),
    "Content-Type": "application/json; charset=utf-8",
    "Accept-Encoding": "gzip, deflate",
}


class Form(object):
    def __init__(self, form_id):
        self._form_id = form_id

    @property
    def id(self):
        return self._form_id

    def get(self, params):
        pass

    def complete_entries(self, params):
        pass

    def incomplete_entries(self, params):
        pass

    def list(self):
        pass


class TypeForm(object):
    def __init__(self, base_uri=None, api_key=None):
        self._base_uri = base_uri
        self._api_key = api_key

    @property
    def api_key(self):
        return self._api_key

    @property
    def base_uri(self):
        return self._base_uri

    def set_api_key(self, key):
        self._api_key = key

    def set_base_uri(self, uri):
        self._base_uri = uri

    def handle_response(self, response):
        if response.code == 400:
            raise BadRequest(response)
        elif response.code == 401:
            raise UnauthorizedAccess()
        elif response.code == 404:
            raise NotFound()
        elif response.code in range(400, 500):
            raise ClientError(response)
        elif response.code in range(500, 600):
            raise ServerError()


import pdb;

pdb.set_trace()
