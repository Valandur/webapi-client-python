# coding: utf-8

"""
    Web-API

    Access Sponge powered Minecraft servers through a WebAPI  # Introduction This is the documentation of the various API routes offered by the WebAPI plugin.  This documentation assumes that you are familiar with the basic concepts of Web API's, such as `GET`, `PUT`, `POST` and `DELETE` methods, request `HEADERS` and `RESPONSE CODES` and `JSON` data.  By default this documentation can be found at http:/localhost:8080 (while your minecraft server is running) and the various routes start with http:/localhost:8080/api/v5...  As a quick test try reaching the route http:/localhost:8080/api/v5/info (remember that you can only access \\\"localhost\\\" routes on the server on which you are running minecraft). This route should show you basic information about your server, like the motd and player count.  # List endpoints Lots of objects offer an endpoint to list all objects (e.g. `GET: /world` to get all worlds). These endpoints return only the properties marked 'required' by default, because the list might be quite large. If you want to return ALL data for a list endpoint add the query parameter `details`, (e.g. `GET: /world?details`).  > Remember that in this case the data returned by the endpoint might be quite large.  # Debugging endpoints Apart from the `?details` flag you can also pass some other flags for debugging purposes. Remember that you must include the first query parameter with `?`, and further ones with `&`:  `details`: Includes details for list endpoints  `accept=[json/xml]`: Manually set the accept content type. This is good for browser testing, **BUT DON'T USE THIS IN PRODUCTION, YOU CAN SUPPLY THE `Accepts` HEADER FOR THAT**  `pretty`: Pretty prints the data, also good for debugging in the browser.  An example request might look like this: `http://localhost:8080/api/v5/world?details&accpet=json&pretty&key=MY-API-KEY`  # Additional data Certain endpoints (such as `/player`, `/entity` and `/tile-entity` have additional properties which are not documented here, because the data depends on the concrete object type (eg. `Sheep` have a wool color, others do not) and on the other plugins/mods that are running on your server which might add additional data.  You can also find more information in the github docs (https:/github.com/Valandur/Web-API/tree/master/docs/DATA.md)  # noqa: E501

    OpenAPI spec version: 5.4.2-S7.1.0
    Contact: inithilian@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.mega_menus_element import MegaMenusElement  # noqa: F401,E501


class MenuMenusMenu(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'link': 'str',
        'elements': 'dict(str, MegaMenusElement)',
        'pages': 'int',
        'title': 'str'
    }

    attribute_map = {
        'link': 'link',
        'elements': 'elements',
        'pages': 'pages',
        'title': 'title'
    }

    def __init__(self, link=None, elements=None, pages=None, title=None):  # noqa: E501
        """MenuMenusMenu - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._elements = None
        self._pages = None
        self._title = None
        self.discriminator = None

        self.link = link
        if elements is not None:
            self.elements = elements
        if pages is not None:
            self.pages = pages
        if title is not None:
            self.title = title

    @property
    def link(self):
        """Gets the link of this MenuMenusMenu.  # noqa: E501

        The API link that can be used to obtain more information about this object  # noqa: E501

        :return: The link of this MenuMenusMenu.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this MenuMenusMenu.

        The API link that can be used to obtain more information about this object  # noqa: E501

        :param link: The link of this MenuMenusMenu.  # noqa: E501
        :type: str
        """
        if link is None:
            raise ValueError("Invalid value for `link`, must not be `None`")  # noqa: E501

        self._link = link

    @property
    def elements(self):
        """Gets the elements of this MenuMenusMenu.  # noqa: E501

        Flattened list of all element in this menu  # noqa: E501

        :return: The elements of this MenuMenusMenu.  # noqa: E501
        :rtype: dict(str, MegaMenusElement)
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this MenuMenusMenu.

        Flattened list of all element in this menu  # noqa: E501

        :param elements: The elements of this MenuMenusMenu.  # noqa: E501
        :type: dict(str, MegaMenusElement)
        """

        self._elements = elements

    @property
    def pages(self):
        """Gets the pages of this MenuMenusMenu.  # noqa: E501

        Get the amount of pages for this menu  # noqa: E501

        :return: The pages of this MenuMenusMenu.  # noqa: E501
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this MenuMenusMenu.

        Get the amount of pages for this menu  # noqa: E501

        :param pages: The pages of this MenuMenusMenu.  # noqa: E501
        :type: int
        """

        self._pages = pages

    @property
    def title(self):
        """Gets the title of this MenuMenusMenu.  # noqa: E501

        The title of this menu  # noqa: E501

        :return: The title of this MenuMenusMenu.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MenuMenusMenu.

        The title of this menu  # noqa: E501

        :param title: The title of this MenuMenusMenu.  # noqa: E501
        :type: str
        """

        self._title = title

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MenuMenusMenu):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other