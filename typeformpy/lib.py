import requests


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
    def __init__(self, base_uri, api_key):
        self.base_uri = base_uri
        self.api_key = api_key

import pdb; pdb.set_trace()