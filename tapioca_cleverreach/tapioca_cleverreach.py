# coding: utf-8
import requests
from django.conf import settings
from requests_oauthlib import OAuth2
from tapioca import (
    TapiocaAdapter, JSONAdapterMixin)
from tapioca.tapioca import TapiocaClient

from .resource_mapping import RESOURCE_MAPPING

api_root = 'https://rest.cleverreach.com/v2/'


def login():
    response = requests.post(api_root + 'login.json', {
        'client_id': settings.CR_CLIENT_ID,
        'login': settings.CR_LOGIN,
        'password': settings.CR_PASSWORD,
    })

    return response.json()


class CleverreachInstantiator(object):
    def __init__(self, adapter_class, token):
        self.adapter_class = adapter_class
        self.token = token
        print('Initial token: %s' % token)

    def __call__(self, serializer_class=None, session=None, **kwargs):
        refresh_token_default = kwargs.pop('refresh_token_by_default', False)
        kwargs['token'] = self.token
        return TapiocaClient(
            self.adapter_class(serializer_class=serializer_class),
            api_params=kwargs, refresh_token_by_default=refresh_token_default,
            session=session)


def generate_wrapper_from_adapter(adapter_class):
    token = login()
    return CleverreachInstantiator(adapter_class, token)


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
        api_params['token'] = login()
        if settings.DEBUG:
            print('Updated token: %s' % api_params['token'])
        return api_params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass


Cleverreach = generate_wrapper_from_adapter(CleverreachClientAdapter)
