# coding: utf-8

"""
    Web-API

    Access Sponge powered Minecraft servers through a WebAPI  # Introduction This is the documentation of the various API routes offered by the WebAPI plugin.  This documentation assumes that you are familiar with the basic concepts of Web API's, such as `GET`, `PUT`, `POST` and `DELETE` methods, request `HEADERS` and `RESPONSE CODES` and `JSON` data.  By default this documentation can be found at http:/localhost:8080 (while your minecraft server is running) and the various routes start with http:/localhost:8080/api/v5...  As a quick test try reaching the route http:/localhost:8080/api/v5/info (remember that you can only access \\\"localhost\\\" routes on the server on which you are running minecraft). This route should show you basic information about your server, like the motd and player count.  # List endpoints Lots of objects offer an endpoint to list all objects (e.g. `GET: /world` to get all worlds). These endpoints return only the properties marked 'required' by default, because the list might be quite large. If you want to return ALL data for a list endpoint add the query parameter `details`, (e.g. `GET: /world?details`).  > Remember that in this case the data returned by the endpoint might be quite large.  # Debugging endpoints Apart from the `?details` flag you can also pass some other flags for debugging purposes. Remember that you must include the first query parameter with `?`, and further ones with `&`:  `details`: Includes details for list endpoints  `accept=[json/xml]`: Manually set the accept content type. This is good for browser testing, **BUT DON'T USE THIS IN PRODUCTION, YOU CAN SUPPLY THE `Accepts` HEADER FOR THAT**  `pretty`: Pretty prints the data, also good for debugging in the browser.  An example request might look like this: `http://localhost:8080/api/v5/world?details&accpet=json&pretty&key=MY-API-KEY`  # Additional data Certain endpoints (such as `/player`, `/entity` and `/tile-entity` have additional properties which are not documented here, because the data depends on the concrete object type (eg. `Sheep` have a wool color, others do not) and on the other plugins/mods that are running on your server which might add additional data.  You can also find more information in the github docs (https:/github.com/Valandur/Web-API/tree/master/docs/DATA.md)  # noqa: E501

    OpenAPI spec version: 5.4.2-S7.1.0
    Contact: inithilian@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.inventory_api import InventoryApi  # noqa: E501
from swagger_client.rest import ApiException


class TestInventoryApi(unittest.TestCase):
    """InventoryApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.inventory_api.InventoryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_element(self):
        """Test case for add_element

        Add element  # noqa: E501
        """
        pass

    def test_close_renderer(self):
        """Test case for close_renderer

        Close renderer  # noqa: E501
        """
        pass

    def test_create_menu(self):
        """Test case for create_menu

        Create menu  # noqa: E501
        """
        pass

    def test_create_renderer(self):
        """Test case for create_renderer

        Create menu  # noqa: E501
        """
        pass

    def test_delete_element(self):
        """Test case for delete_element

        Delete menu  # noqa: E501
        """
        pass

    def test_delete_menu(self):
        """Test case for delete_menu

        Delete menu  # noqa: E501
        """
        pass

    def test_delete_page(self):
        """Test case for delete_page

        Delete a page of elements  # noqa: E501
        """
        pass

    def test_delete_renderer(self):
        """Test case for delete_renderer

        Delete menu  # noqa: E501
        """
        pass

    def test_find_renderer(self):
        """Test case for find_renderer

        Get the renderer for viewer  # noqa: E501
        """
        pass

    def test_get_element(self):
        """Test case for get_element

        Get menu  # noqa: E501
        """
        pass

    def test_get_menu(self):
        """Test case for get_menu

        Get menu  # noqa: E501
        """
        pass

    def test_get_page(self):
        """Test case for get_page

        Reads a single page of elements  # noqa: E501
        """
        pass

    def test_get_renderer(self):
        """Test case for get_renderer

        Get the renderer for this menu  # noqa: E501
        """
        pass

    def test_list_menus(self):
        """Test case for list_menus

        List menus  # noqa: E501
        """
        pass

    def test_list_renderer(self):
        """Test case for list_renderer

        List renderer  # noqa: E501
        """
        pass

    def test_open_renderer(self):
        """Test case for open_renderer

        Open renderer  # noqa: E501
        """
        pass

    def test_set_element(self):
        """Test case for set_element

        Update menu  # noqa: E501
        """
        pass

    def test_set_menu(self):
        """Test case for set_menu

        Update menu  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
