# coding: utf-8

"""
    WebAPI

    Access Sponge powered Minecraft servers through a WebAPI  # Introduction This is the documentation of the various API routes offered by the WebAPI plugin.  This documentation assumes that you are familiar with the basic concepts of Web API's, such as `GET`, `PUT`, `POST` and `DELETE` methods, request `HEADERS` and `RESPONSE CODES` and `JSON` data.  By default this documentation can be found at http:/localhost:8080 (while your minecraft server is running) and the various routes start with http:/localhost:8080/api/...  As a quick test try reaching the route http:/localhost:8080/api/info (remember that you can only access \"localhost\" routes on the server on which you are running minecraft). This route should show you basic information about your server, like the motd and player count.  # Additional data Certain endpoints (such as `/player`, `/entity` and `/tile-entity` have additional properties which are not documented here, because the data depends on the concrete object type (eg. `Sheep` have a wool color, others do not) and on the other plugins/mods that are running on your server which might add additional data.  You can also find more information in the github docs (https:/github.com/Valandur/Web-API/tree/master/docs/DATA.md) 

    OpenAPI spec version: <version>
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UpdateEntityRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'world': 'str',
        'position': 'Vector3',
        'velocity': 'Vector3',
        'rotation': 'Vector3',
        'scale': 'Vector3',
        'damage': 'DamageRequest'
    }

    attribute_map = {
        'world': 'world',
        'position': 'position',
        'velocity': 'velocity',
        'rotation': 'rotation',
        'scale': 'scale',
        'damage': 'damage'
    }

    def __init__(self, world=None, position=None, velocity=None, rotation=None, scale=None, damage=None):
        """
        UpdateEntityRequest - a model defined in Swagger
        """

        self._world = None
        self._position = None
        self._velocity = None
        self._rotation = None
        self._scale = None
        self._damage = None

        if world is not None:
          self.world = world
        if position is not None:
          self.position = position
        if velocity is not None:
          self.velocity = velocity
        if rotation is not None:
          self.rotation = rotation
        if scale is not None:
          self.scale = scale
        if damage is not None:
          self.damage = damage

    @property
    def world(self):
        """
        Gets the world of this UpdateEntityRequest.
        The UUID or name of the world that the entity is moved to.

        :return: The world of this UpdateEntityRequest.
        :rtype: str
        """
        return self._world

    @world.setter
    def world(self, world):
        """
        Sets the world of this UpdateEntityRequest.
        The UUID or name of the world that the entity is moved to.

        :param world: The world of this UpdateEntityRequest.
        :type: str
        """

        self._world = world

    @property
    def position(self):
        """
        Gets the position of this UpdateEntityRequest.

        :return: The position of this UpdateEntityRequest.
        :rtype: Vector3
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this UpdateEntityRequest.

        :param position: The position of this UpdateEntityRequest.
        :type: Vector3
        """

        self._position = position

    @property
    def velocity(self):
        """
        Gets the velocity of this UpdateEntityRequest.

        :return: The velocity of this UpdateEntityRequest.
        :rtype: Vector3
        """
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        """
        Sets the velocity of this UpdateEntityRequest.

        :param velocity: The velocity of this UpdateEntityRequest.
        :type: Vector3
        """

        self._velocity = velocity

    @property
    def rotation(self):
        """
        Gets the rotation of this UpdateEntityRequest.

        :return: The rotation of this UpdateEntityRequest.
        :rtype: Vector3
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """
        Sets the rotation of this UpdateEntityRequest.

        :param rotation: The rotation of this UpdateEntityRequest.
        :type: Vector3
        """

        self._rotation = rotation

    @property
    def scale(self):
        """
        Gets the scale of this UpdateEntityRequest.

        :return: The scale of this UpdateEntityRequest.
        :rtype: Vector3
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """
        Sets the scale of this UpdateEntityRequest.

        :param scale: The scale of this UpdateEntityRequest.
        :type: Vector3
        """

        self._scale = scale

    @property
    def damage(self):
        """
        Gets the damage of this UpdateEntityRequest.

        :return: The damage of this UpdateEntityRequest.
        :rtype: DamageRequest
        """
        return self._damage

    @damage.setter
    def damage(self, damage):
        """
        Sets the damage of this UpdateEntityRequest.

        :param damage: The damage of this UpdateEntityRequest.
        :type: DamageRequest
        """

        self._damage = damage

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, UpdateEntityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
