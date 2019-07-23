# coding: utf-8

"""
    Web-API

    Access Sponge powered Minecraft servers through a WebAPI  # Introduction This is the documentation of the various API routes offered by the WebAPI plugin.  This documentation assumes that you are familiar with the basic concepts of Web API's, such as `GET`, `PUT`, `POST` and `DELETE` methods, request `HEADERS` and `RESPONSE CODES` and `JSON` data.  By default this documentation can be found at http:/localhost:8080 (while your minecraft server is running) and the various routes start with http:/localhost:8080/api/v5...  As a quick test try reaching the route http:/localhost:8080/api/v5/info (remember that you can only access \\\"localhost\\\" routes on the server on which you are running minecraft). This route should show you basic information about your server, like the motd and player count.  # List endpoints Lots of objects offer an endpoint to list all objects (e.g. `GET: /world` to get all worlds). These endpoints return only the properties marked 'required' by default, because the list might be quite large. If you want to return ALL data for a list endpoint add the query parameter `details`, (e.g. `GET: /world?details`).  > Remember that in this case the data returned by the endpoint might be quite large.  # Debugging endpoints Apart from the `?details` flag you can also pass some other flags for debugging purposes. Remember that you must include the first query parameter with `?`, and further ones with `&`:  `details`: Includes details for list endpoints  `accept=[json/xml]`: Manually set the accept content type. This is good for browser testing, **BUT DON'T USE THIS IN PRODUCTION, YOU CAN SUPPLY THE `Accepts` HEADER FOR THAT**  `pretty`: Pretty prints the data, also good for debugging in the browser.  An example request might look like this: `http://localhost:8080/api/v5/world?details&accpet=json&pretty&key=MY-API-KEY`  # Additional data Certain endpoints (such as `/player`, `/entity` and `/tile-entity` have additional properties which are not documented here, because the data depends on the concrete object type (eg. `Sheep` have a wool color, others do not) and on the other plugins/mods that are running on your server which might add additional data.  You can also find more information in the github docs (https:/github.com/Valandur/Web-API/tree/master/docs/DATA.md)  # noqa: E501

    OpenAPI spec version: 5.4.2-S7.1.0
    Contact: inithilian@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ChunkApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_chunk_at(self, world, x, z, **kwargs):  # noqa: E501
        """Load & Generate a chunk  # noqa: E501

        Forces a chunk to be loaded into memory, and created if it does not exist.     **Required permissions:**    - **chunk.create**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_chunk_at(world, x, z, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str world: The uuid of the world in which to create the chunk (required)
        :param int x: The x-coordinate of the chunk (in chunk coordinates) (required)
        :param int z: The z-coordinate of the chunk (in chunk coordinates) (required)
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: Chunk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_chunk_at_with_http_info(world, x, z, **kwargs)  # noqa: E501
        else:
            (data) = self.create_chunk_at_with_http_info(world, x, z, **kwargs)  # noqa: E501
            return data

    def create_chunk_at_with_http_info(self, world, x, z, **kwargs):  # noqa: E501
        """Load & Generate a chunk  # noqa: E501

        Forces a chunk to be loaded into memory, and created if it does not exist.     **Required permissions:**    - **chunk.create**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_chunk_at_with_http_info(world, x, z, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str world: The uuid of the world in which to create the chunk (required)
        :param int x: The x-coordinate of the chunk (in chunk coordinates) (required)
        :param int z: The z-coordinate of the chunk (in chunk coordinates) (required)
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: Chunk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['world', 'x', 'z', 'details', 'accept', 'pretty']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_chunk_at" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'world' is set
        if ('world' not in params or
                params['world'] is None):
            raise ValueError("Missing the required parameter `world` when calling `create_chunk_at`")  # noqa: E501
        # verify the required parameter 'x' is set
        if ('x' not in params or
                params['x'] is None):
            raise ValueError("Missing the required parameter `x` when calling `create_chunk_at`")  # noqa: E501
        # verify the required parameter 'z' is set
        if ('z' not in params or
                params['z'] is None):
            raise ValueError("Missing the required parameter `z` when calling `create_chunk_at`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'world' in params:
            path_params['world'] = params['world']  # noqa: E501
        if 'x' in params:
            path_params['x'] = params['x']  # noqa: E501
        if 'z' in params:
            path_params['z'] = params['z']  # noqa: E501

        query_params = []
        if 'details' in params:
            query_params.append(('details', params['details']))  # noqa: E501
        if 'accept' in params:
            query_params.append(('accept', params['accept']))  # noqa: E501
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeader', 'ApiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/chunk/{world}/{x}/{z}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Chunk',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_chunk_at(self, world, x, z, **kwargs):  # noqa: E501
        """Get a chunk  # noqa: E501

        Get detailed information about a chunk     **Required permissions:**    - **chunk.one**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chunk_at(world, x, z, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str world: The uuid of the world in which to get the chunk (required)
        :param int x: The x-coordinate of the chunk (in chunk coordinates) (required)
        :param int z: The z-coordinate of the chunk (in chunk coordinates) (required)
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: Chunk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_chunk_at_with_http_info(world, x, z, **kwargs)  # noqa: E501
        else:
            (data) = self.get_chunk_at_with_http_info(world, x, z, **kwargs)  # noqa: E501
            return data

    def get_chunk_at_with_http_info(self, world, x, z, **kwargs):  # noqa: E501
        """Get a chunk  # noqa: E501

        Get detailed information about a chunk     **Required permissions:**    - **chunk.one**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chunk_at_with_http_info(world, x, z, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str world: The uuid of the world in which to get the chunk (required)
        :param int x: The x-coordinate of the chunk (in chunk coordinates) (required)
        :param int z: The z-coordinate of the chunk (in chunk coordinates) (required)
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: Chunk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['world', 'x', 'z', 'details', 'accept', 'pretty']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chunk_at" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'world' is set
        if ('world' not in params or
                params['world'] is None):
            raise ValueError("Missing the required parameter `world` when calling `get_chunk_at`")  # noqa: E501
        # verify the required parameter 'x' is set
        if ('x' not in params or
                params['x'] is None):
            raise ValueError("Missing the required parameter `x` when calling `get_chunk_at`")  # noqa: E501
        # verify the required parameter 'z' is set
        if ('z' not in params or
                params['z'] is None):
            raise ValueError("Missing the required parameter `z` when calling `get_chunk_at`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'world' in params:
            path_params['world'] = params['world']  # noqa: E501
        if 'x' in params:
            path_params['x'] = params['x']  # noqa: E501
        if 'z' in params:
            path_params['z'] = params['z']  # noqa: E501

        query_params = []
        if 'details' in params:
            query_params.append(('details', params['details']))  # noqa: E501
        if 'accept' in params:
            query_params.append(('accept', params['accept']))  # noqa: E501
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeader', 'ApiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/chunk/{world}/{x}/{z}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Chunk',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_chunks(self, world, **kwargs):  # noqa: E501
        """List chunks  # noqa: E501

        Gets a list of all the loaded chunks for the specified world.     **Required permissions:**    - **chunk.list**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_chunks(world, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str world: The uuid of the for which to get all chunks (required)
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: list[Chunk]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_chunks_with_http_info(world, **kwargs)  # noqa: E501
        else:
            (data) = self.list_chunks_with_http_info(world, **kwargs)  # noqa: E501
            return data

    def list_chunks_with_http_info(self, world, **kwargs):  # noqa: E501
        """List chunks  # noqa: E501

        Gets a list of all the loaded chunks for the specified world.     **Required permissions:**    - **chunk.list**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_chunks_with_http_info(world, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str world: The uuid of the for which to get all chunks (required)
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: list[Chunk]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['world', 'details', 'accept', 'pretty']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_chunks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'world' is set
        if ('world' not in params or
                params['world'] is None):
            raise ValueError("Missing the required parameter `world` when calling `list_chunks`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'world' in params:
            path_params['world'] = params['world']  # noqa: E501

        query_params = []
        if 'details' in params:
            query_params.append(('details', params['details']))  # noqa: E501
        if 'accept' in params:
            query_params.append(('accept', params['accept']))  # noqa: E501
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeader', 'ApiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/chunk/{world}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Chunk]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
