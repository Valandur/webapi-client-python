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

from swagger_client.models.catalog_type import CatalogType  # noqa: F401,E501
from swagger_client.models.color import Color  # noqa: F401,E501


class FireworkEffect(object):
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
        'shape': 'CatalogType',
        'flickers': 'bool',
        'colors': 'list[Color]',
        'fade_colors': 'list[Color]',
        'trail': 'bool'
    }

    attribute_map = {
        'shape': 'shape',
        'flickers': 'flickers',
        'colors': 'colors',
        'fade_colors': 'fadeColors',
        'trail': 'trail'
    }

    def __init__(self, shape=None, flickers=None, colors=None, fade_colors=None, trail=None):  # noqa: E501
        """FireworkEffect - a model defined in Swagger"""  # noqa: E501

        self._shape = None
        self._flickers = None
        self._colors = None
        self._fade_colors = None
        self._trail = None
        self.discriminator = None

        self.shape = shape
        self.flickers = flickers
        self.colors = colors
        self.fade_colors = fade_colors
        self.trail = trail

    @property
    def shape(self):
        """Gets the shape of this FireworkEffect.  # noqa: E501

        The shape of the firework  # noqa: E501

        :return: The shape of this FireworkEffect.  # noqa: E501
        :rtype: CatalogType
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this FireworkEffect.

        The shape of the firework  # noqa: E501

        :param shape: The shape of this FireworkEffect.  # noqa: E501
        :type: CatalogType
        """
        if shape is None:
            raise ValueError("Invalid value for `shape`, must not be `None`")  # noqa: E501

        self._shape = shape

    @property
    def flickers(self):
        """Gets the flickers of this FireworkEffect.  # noqa: E501

        True if the firework flickers, false otherwise  # noqa: E501

        :return: The flickers of this FireworkEffect.  # noqa: E501
        :rtype: bool
        """
        return self._flickers

    @flickers.setter
    def flickers(self, flickers):
        """Sets the flickers of this FireworkEffect.

        True if the firework flickers, false otherwise  # noqa: E501

        :param flickers: The flickers of this FireworkEffect.  # noqa: E501
        :type: bool
        """
        if flickers is None:
            raise ValueError("Invalid value for `flickers`, must not be `None`")  # noqa: E501

        self._flickers = flickers

    @property
    def colors(self):
        """Gets the colors of this FireworkEffect.  # noqa: E501

        The colors that make up this firework  # noqa: E501

        :return: The colors of this FireworkEffect.  # noqa: E501
        :rtype: list[Color]
        """
        return self._colors

    @colors.setter
    def colors(self, colors):
        """Sets the colors of this FireworkEffect.

        The colors that make up this firework  # noqa: E501

        :param colors: The colors of this FireworkEffect.  # noqa: E501
        :type: list[Color]
        """
        if colors is None:
            raise ValueError("Invalid value for `colors`, must not be `None`")  # noqa: E501

        self._colors = colors

    @property
    def fade_colors(self):
        """Gets the fade_colors of this FireworkEffect.  # noqa: E501

        The fade colors that this firework has  # noqa: E501

        :return: The fade_colors of this FireworkEffect.  # noqa: E501
        :rtype: list[Color]
        """
        return self._fade_colors

    @fade_colors.setter
    def fade_colors(self, fade_colors):
        """Sets the fade_colors of this FireworkEffect.

        The fade colors that this firework has  # noqa: E501

        :param fade_colors: The fade_colors of this FireworkEffect.  # noqa: E501
        :type: list[Color]
        """
        if fade_colors is None:
            raise ValueError("Invalid value for `fade_colors`, must not be `None`")  # noqa: E501

        self._fade_colors = fade_colors

    @property
    def trail(self):
        """Gets the trail of this FireworkEffect.  # noqa: E501

        True if this firework has a trail, false otherwise  # noqa: E501

        :return: The trail of this FireworkEffect.  # noqa: E501
        :rtype: bool
        """
        return self._trail

    @trail.setter
    def trail(self, trail):
        """Sets the trail of this FireworkEffect.

        True if this firework has a trail, false otherwise  # noqa: E501

        :param trail: The trail of this FireworkEffect.  # noqa: E501
        :type: bool
        """
        if trail is None:
            raise ValueError("Invalid value for `trail`, must not be `None`")  # noqa: E501

        self._trail = trail

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
        if not isinstance(other, FireworkEffect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
