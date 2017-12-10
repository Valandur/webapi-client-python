# coding: utf-8

"""
    WebAPI

    Access Sponge powered Minecraft servers through a WebAPI  # Introduction This is the documentation of the various API routes offered by the WebAPI plugin.  This documentation assumes that you are familiar with the basic concepts of Web API's, such as `GET`, `PUT`, `POST` and `DELETE` methods, request `HEADERS` and `RESPONSE CODES` and `JSON` data.  By default this documentation can be found at http:/localhost:8080 (while your minecraft server is running) and the various routes start with http:/localhost:8080/api/...  As a quick test try reaching the route http:/localhost:8080/api/info (remember that you can only access \"localhost\" routes on the server on which you are running minecraft). This route should show you basic information about your server, like the motd and player count.  # Additional data Certain endpoints (such as `/player`, `/entity` and `/tile-entity` have additional properties which are not documented here, because the data depends on the concrete object type (eg. `Sheep` have a wool color, others do not) and on the other plugins/mods that are running on your server which might add additional data.  You can also find more information in the github docs (https:/github.com/Valandur/Web-API/tree/master/docs/DATA.md) 

    OpenAPI spec version: <version>
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class PlayerApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def change_player(self, uuid, update_player_request, **kwargs):
        """
        Edit player
        Update the properties of an existing player.  > Required permission: player.change 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.change_player(uuid, update_player_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str uuid: The uuid of the player. (required)
        :param UpdatePlayerRequest update_player_request: The new properties of the player (required)
        :return: PlayerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.change_player_with_http_info(uuid, update_player_request, **kwargs)
        else:
            (data) = self.change_player_with_http_info(uuid, update_player_request, **kwargs)
            return data

    def change_player_with_http_info(self, uuid, update_player_request, **kwargs):
        """
        Edit player
        Update the properties of an existing player.  > Required permission: player.change 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.change_player_with_http_info(uuid, update_player_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str uuid: The uuid of the player. (required)
        :param UpdatePlayerRequest update_player_request: The new properties of the player (required)
        :return: PlayerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'update_player_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_player" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params) or (params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `change_player`")
        # verify the required parameter 'update_player_request' is set
        if ('update_player_request' not in params) or (params['update_player_request'] is None):
            raise ValueError("Missing the required parameter `update_player_request` when calling `change_player`")


        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_player_request' in params:
            body_params = params['update_player_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = ['headerKey', 'queryKey']

        return self.api_client.call_api('/player/{uuid}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PlayerResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def execute_player_method(self, uuid, request, **kwargs):
        """
        Execute player method
        Provides direct access to the underlaying player object and can execute any method on it.  > Required permission: player.method 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.execute_player_method(uuid, request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str uuid: The uuid of the player. (required)
        :param RawRequest request: Information about which method to execute. (required)
        :return: ExecutePlayerMethodResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.execute_player_method_with_http_info(uuid, request, **kwargs)
        else:
            (data) = self.execute_player_method_with_http_info(uuid, request, **kwargs)
            return data

    def execute_player_method_with_http_info(self, uuid, request, **kwargs):
        """
        Execute player method
        Provides direct access to the underlaying player object and can execute any method on it.  > Required permission: player.method 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.execute_player_method_with_http_info(uuid, request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str uuid: The uuid of the player. (required)
        :param RawRequest request: Information about which method to execute. (required)
        :return: ExecutePlayerMethodResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method execute_player_method" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params) or (params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `execute_player_method`")
        # verify the required parameter 'request' is set
        if ('request' not in params) or (params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `execute_player_method`")


        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = ['headerKey', 'queryKey']

        return self.api_client.call_api('/player/{uuid}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ExecutePlayerMethodResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_player(self, uuid, **kwargs):
        """
        Detailed player info
        Get detailed information about a player.  > Required permission: player.one 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_player(uuid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str uuid: The uuid of the player to get detailed information about. (required)
        :param str fields: An optional list of additional fields to get.
        :param str methods: An optional list of additional methods to get.
        :return: PlayerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_player_with_http_info(uuid, **kwargs)
        else:
            (data) = self.get_player_with_http_info(uuid, **kwargs)
            return data

    def get_player_with_http_info(self, uuid, **kwargs):
        """
        Detailed player info
        Get detailed information about a player.  > Required permission: player.one 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_player_with_http_info(uuid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str uuid: The uuid of the player to get detailed information about. (required)
        :param str fields: An optional list of additional fields to get.
        :param str methods: An optional list of additional methods to get.
        :return: PlayerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'fields', 'methods']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_player" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params) or (params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `get_player`")


        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))
        if 'methods' in params:
            query_params.append(('methods', params['methods']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = ['headerKey', 'queryKey']

        return self.api_client.call_api('/player/{uuid}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PlayerResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_players(self, **kwargs):
        """
        Player list
        Get a list of all the players on the server.  > Required permission: player.list 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_players(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: PlayersList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_players_with_http_info(**kwargs)
        else:
            (data) = self.get_players_with_http_info(**kwargs)
            return data

    def get_players_with_http_info(self, **kwargs):
        """
        Player list
        Get a list of all the players on the server.  > Required permission: player.list 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_players_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: PlayersList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_players" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = ['headerKey', 'queryKey']

        return self.api_client.call_api('/player', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PlayersList',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
