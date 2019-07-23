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

from swagger_client.models.vector3d import Vector3d  # noqa: F401,E501
from swagger_client.models.world import World  # noqa: F401,E501


class Transform(object):
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
        'world': 'World',
        'position': 'Vector3d',
        'rotation': 'Vector3d',
        'scale': 'Vector3d'
    }

    attribute_map = {
        'world': 'world',
        'position': 'position',
        'rotation': 'rotation',
        'scale': 'scale'
    }

    def __init__(self, world=None, position=None, rotation=None, scale=None):  # noqa: E501
        """Transform - a model defined in Swagger"""  # noqa: E501

        self._world = None
        self._position = None
        self._rotation = None
        self._scale = None
        self.discriminator = None

        self.world = world
        self.position = position
        self.rotation = rotation
        self.scale = scale

    @property
    def world(self):
        """Gets the world of this Transform.  # noqa: E501

        The world of this transform  # noqa: E501

        :return: The world of this Transform.  # noqa: E501
        :rtype: World
        """
        return self._world

    @world.setter
    def world(self, world):
        """Sets the world of this Transform.

        The world of this transform  # noqa: E501

        :param world: The world of this Transform.  # noqa: E501
        :type: World
        """
        if world is None:
            raise ValueError("Invalid value for `world`, must not be `None`")  # noqa: E501

        self._world = world

    @property
    def position(self):
        """Gets the position of this Transform.  # noqa: E501

        The position within the world  # noqa: E501

        :return: The position of this Transform.  # noqa: E501
        :rtype: Vector3d
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Transform.

        The position within the world  # noqa: E501

        :param position: The position of this Transform.  # noqa: E501
        :type: Vector3d
        """
        if position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

    @property
    def rotation(self):
        """Gets the rotation of this Transform.  # noqa: E501

        The rotation of the object  # noqa: E501

        :return: The rotation of this Transform.  # noqa: E501
        :rtype: Vector3d
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this Transform.

        The rotation of the object  # noqa: E501

        :param rotation: The rotation of this Transform.  # noqa: E501
        :type: Vector3d
        """
        if rotation is None:
            raise ValueError("Invalid value for `rotation`, must not be `None`")  # noqa: E501

        self._rotation = rotation

    @property
    def scale(self):
        """Gets the scale of this Transform.  # noqa: E501

        The scale of the object  # noqa: E501

        :return: The scale of this Transform.  # noqa: E501
        :rtype: Vector3d
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this Transform.

        The scale of the object  # noqa: E501

        :param scale: The scale of this Transform.  # noqa: E501
        :type: Vector3d
        """
        if scale is None:
            raise ValueError("Invalid value for `scale`, must not be `None`")  # noqa: E501

        self._scale = scale

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
        if issubclass(Transform, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Transform):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
