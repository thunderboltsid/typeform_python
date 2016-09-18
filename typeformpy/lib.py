import requests
import json
from errors import TypeFormError, ClientError, ServerError, BadRequest, \
    UnauthorizedAccess, NotFound, Unavailable


def handle_response(response):
    if response.status_code == 400:
        raise BadRequest(response)
    elif response.status_code == 401:
        raise UnauthorizedAccess()
    elif response.status_code == 404:
        raise NotFound()
    elif response.status_code in range(400, 500):
        raise ClientError(response)
    elif response.status_code in range(500, 600):
        raise ServerError()
    else:
        return response


def get_parameter(key, value):
    return "&" + key + "=" + value


class Form(object):
    def __init__(self, form_id=None, typeform=None):
        self._form_id = form_id
        self._typeform = typeform

    @property
    def id(self):
        return self._form_id

    @property
    def typeform(self):
        return self._typeform

    def query_uri(self, params={}):
        base_uri = self.typeform.base_uri
        form_uri = base_uri + self.id + "?" + "key=" + self.typeform.api_key
        uri = form_uri
        if params != {}:
            for param in params:
                uri += get_parameter(param[0], param[1])
        return uri

    def get(self, params={}):
        if params == {}:
            return handle_response(requests.get(self.query_uri()))
        else:
            return handle_response(requests.get(self.query_uri(params=params)))

    def complete_entries(self, params={}):
        params["complete"] = "true"
        return self.get(params=params)

    def incomplete_entries(self, params={}):
        return self.get(params)


class TypeForm(object):
    def __init__(self, api_key=None,
                 base_uri="https://api.typeform.com/v1/form/"):
        self._base_uri = base_uri
        self._api_key = api_key
        self._form = None

    @property
    def api_key(self):
        return self._api_key

    @property
    def base_uri(self):
        return self._base_uri

    @property
    def form(self):
        return self._form

    def use_form(self, form_id):
        self._form = Form(form_id=form_id, typeform=self)

