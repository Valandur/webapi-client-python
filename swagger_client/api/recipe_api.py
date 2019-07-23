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


class RecipeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_recipes(self, **kwargs):  # noqa: E501
        """List recipes  # noqa: E501

             **Required permissions:**    - **recipe.list**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_recipes(async=True)
        >>> result = thread.get()

        :param async bool
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_recipes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_recipes_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_recipes_with_http_info(self, **kwargs):  # noqa: E501
        """List recipes  # noqa: E501

             **Required permissions:**    - **recipe.list**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_recipes_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['details', 'accept', 'pretty']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_recipes" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/recipe', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
