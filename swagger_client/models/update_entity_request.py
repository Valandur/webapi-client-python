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

from swagger_client.models.damage_request import DamageRequest  # noqa: F401,E501
from swagger_client.models.slot_request import SlotRequest  # noqa: F401,E501
from swagger_client.models.vector3d import Vector3d  # noqa: F401,E501


class UpdateEntityRequest(object):
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
        'damage': 'DamageRequest',
        'inventory': 'list[SlotRequest]',
        'position': 'Vector3d',
        'rotation': 'Vector3d',
        'scale': 'Vector3d',
        'velocity': 'Vector3d',
        'world': 'str'
    }

    attribute_map = {
        'damage': 'damage',
        'inventory': 'inventory',
        'position': 'position',
        'rotation': 'rotation',
        'scale': 'scale',
        'velocity': 'velocity',
        'world': 'world'
    }

    def __init__(self, damage=None, inventory=None, position=None, rotation=None, scale=None, velocity=None, world=None):  # noqa: E501
        """UpdateEntityRequest - a model defined in Swagger"""  # noqa: E501

        self._damage = None
        self._inventory = None
        self._position = None
        self._rotation = None
        self._scale = None
        self._velocity = None
        self._world = None
        self.discriminator = None

        if damage is not None:
            self.damage = damage
        if inventory is not None:
            self.inventory = inventory
        if position is not None:
            self.position = position
        if rotation is not None:
            self.rotation = rotation
        if scale is not None:
            self.scale = scale
        if velocity is not None:
            self.velocity = velocity
        if world is not None:
            self.world = world

    @property
    def damage(self):
        """Gets the damage of this UpdateEntityRequest.  # noqa: E501

        The damage the entity will take  # noqa: E501

        :return: The damage of this UpdateEntityRequest.  # noqa: E501
        :rtype: DamageRequest
        """
        return self._damage

    @damage.setter
    def damage(self, damage):
        """Sets the damage of this UpdateEntityRequest.

        The damage the entity will take  # noqa: E501

        :param damage: The damage of this UpdateEntityRequest.  # noqa: E501
        :type: DamageRequest
        """

        self._damage = damage

    @property
    def inventory(self):
        """Gets the inventory of this UpdateEntityRequest.  # noqa: E501

        The slots in the inventory of the entity to modify  # noqa: E501

        :return: The inventory of this UpdateEntityRequest.  # noqa: E501
        :rtype: list[SlotRequest]
        """
        return self._inventory

    @inventory.setter
    def inventory(self, inventory):
        """Sets the inventory of this UpdateEntityRequest.

        The slots in the inventory of the entity to modify  # noqa: E501

        :param inventory: The inventory of this UpdateEntityRequest.  # noqa: E501
        :type: list[SlotRequest]
        """

        self._inventory = inventory

    @property
    def position(self):
        """Gets the position of this UpdateEntityRequest.  # noqa: E501

        The position that the entity will be moved to  # noqa: E501

        :return: The position of this UpdateEntityRequest.  # noqa: E501
        :rtype: Vector3d
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this UpdateEntityRequest.

        The position that the entity will be moved to  # noqa: E501

        :param position: The position of this UpdateEntityRequest.  # noqa: E501
        :type: Vector3d
        """

        self._position = position

    @property
    def rotation(self):
        """Gets the rotation of this UpdateEntityRequest.  # noqa: E501

        The new rotation of the entity  # noqa: E501

        :return: The rotation of this UpdateEntityRequest.  # noqa: E501
        :rtype: Vector3d
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this UpdateEntityRequest.

        The new rotation of the entity  # noqa: E501

        :param rotation: The rotation of this UpdateEntityRequest.  # noqa: E501
        :type: Vector3d
        """

        self._rotation = rotation

    @property
    def scale(self):
        """Gets the scale of this UpdateEntityRequest.  # noqa: E501

        The new scale of the entity  # noqa: E501

        :return: The scale of this UpdateEntityRequest.  # noqa: E501
        :rtype: Vector3d
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this UpdateEntityRequest.

        The new scale of the entity  # noqa: E501

        :param scale: The scale of this UpdateEntityRequest.  # noqa: E501
        :type: Vector3d
        """

        self._scale = scale

    @property
    def velocity(self):
        """Gets the velocity of this UpdateEntityRequest.  # noqa: E501

        The new speed of the entity  # noqa: E501

        :return: The velocity of this UpdateEntityRequest.  # noqa: E501
        :rtype: Vector3d
        """
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        """Sets the velocity of this UpdateEntityRequest.

        The new speed of the entity  # noqa: E501

        :param velocity: The velocity of this UpdateEntityRequest.  # noqa: E501
        :type: Vector3d
        """

        self._velocity = velocity

    @property
    def world(self):
        """Gets the world of this UpdateEntityRequest.  # noqa: E501

        The world that the entity will be moved to  # noqa: E501

        :return: The world of this UpdateEntityRequest.  # noqa: E501
        :rtype: str
        """
        return self._world

    @world.setter
    def world(self, world):
        """Sets the world of this UpdateEntityRequest.

        The world that the entity will be moved to  # noqa: E501

        :param world: The world of this UpdateEntityRequest.  # noqa: E501
        :type: str
        """

        self._world = world

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
        if issubclass(UpdateEntityRequest, dict):
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
        if not isinstance(other, UpdateEntityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
