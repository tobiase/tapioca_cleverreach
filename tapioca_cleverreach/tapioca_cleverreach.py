# coding: utf-8
import requests
from requests_oauthlib import OAuth2
from tapioca import (
    TapiocaAdapter, JSONAdapterMixin)
from tapioca.tapioca import TapiocaClient

from .exceptions import CleverreachTokenAcquireException
from .resource_mapping import RESOURCE_MAPPING

api_root = 'https://rest.cleverreach.com/v2/'


def acquire_token(client_id, login, password, **kwargs):
    response = requests.post(api_root + 'login.json', {
        'client_id': client_id,
        'login': login,
        'password': password,
    })

    if 500 <= response.status_code < 600:
        raise CleverreachTokenAcquireException(response)

    data = response.json()
    if 400 <= response.status_code < 500:
        raise CleverreachTokenAcquireException(response, data)

    return data


class CleverreachInstantiator(object):

    def __init__(self, adapter_class):
        self.adapter_class = adapter_class

    def __call__(self, serializer_class=None, session=None, **kwargs):
        refresh_token_default = kwargs.pop('refresh_token_by_default', False)
        kwargs['token'] = acquire_token(**kwargs)
        return TapiocaClient(
            self.adapter_class(serializer_class=serializer_class),
            api_params=kwargs, refresh_token_by_default=refresh_token_default,
            session=session)


def generate_wrapper_from_adapter(adapter_class):
    return CleverreachInstantiator(adapter_class)


class CleverreachClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://rest.cleverreach.com/v2/'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(CleverreachClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        params['auth'] = OAuth2(
            api_params.get('client_id', ''), token={
                'access_token': api_params.get('token', ''),
                'token_type': 'Bearer'})

        return params

    def is_authentication_expired(self, exception, *args, **kwargs):
        """
        Todo: Find proper way to detect expired token and don't just assume it.
        """
        return True

    def refresh_authentication(self, api_params, *args, **kwargs):
        api_params['token'] = acquire_token(**api_params)
        return api_params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass


Cleverreach = generate_wrapper_from_adapter(CleverreachClientAdapter)
