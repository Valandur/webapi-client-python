# coding: utf-8

"""
    WebAPI

    Access Sponge powered Minecraft servers through a WebAPI  # Introduction This is the documentation of the various API routes offered by the WebAPI plugin.  This documentation assumes that you are familiar with the basic concepts of Web API's, such as `GET`, `PUT`, `POST` and `DELETE` methods, request `HEADERS` and `RESPONSE CODES` and `JSON` data.  By default this documentation can be found at http:/localhost:8080 (while your minecraft server is running) and the various routes start with http:/localhost:8080/api/...  As a quick test try reaching the route http:/localhost:8080/api/info (remember that you can only access \"localhost\" routes on the server on which you are running minecraft). This route should show you basic information about your server, like the motd and player count.  # Additional data Certain endpoints (such as `/player`, `/entity` and `/tile-entity` have additional properties which are not documented here, because the data depends on the concrete object type (eg. `Sheep` have a wool color, others do not) and on the other plugins/mods that are running on your server which might add additional data.  You can also find more information in the github docs (https:/github.com/Valandur/Web-API/tree/master/docs/DATA.md) 

    OpenAPI spec version: <version>
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.world_api import WorldApi


class TestWorldApi(unittest.TestCase):
    """ WorldApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.world_api.WorldApi()

    def tearDown(self):
        pass

    def test_change_world(self):
        """
        Test case for change_world

        Edit world
        """
        pass

    def test_create_world(self):
        """
        Test case for create_world

        Create a world
        """
        pass

    def test_delete_world(self):
        """
        Test case for delete_world

        Delete a world
        """
        pass

    def test_execute_world_method(self):
        """
        Test case for execute_world_method

        Execute world methods
        """
        pass

    def test_get_chunk(self):
        """
        Test case for get_chunk

        Detailed chunk info
        """
        pass

    def test_get_chunks(self):
        """
        Test case for get_chunks

        Loaded chunk list
        """
        pass

    def test_get_world(self):
        """
        Test case for get_world

        Detailed world info
        """
        pass

    def test_get_worlds(self):
        """
        Test case for get_worlds

        World list
        """
        pass


if __name__ == '__main__':
    unittest.main()
