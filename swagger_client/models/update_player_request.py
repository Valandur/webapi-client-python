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


class UpdatePlayerRequest(object):
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
        'exhaustion': 'float',
        'experience_since_level': 'int',
        'food_level': 'int',
        'game_mode': 'str',
        'health': 'float',
        'inventory': 'list[SlotRequest]',
        'level': 'int',
        'max_health': 'float',
        'position': 'Vector3d',
        'rotation': 'Vector3d',
        'saturation': 'float',
        'scale': 'Vector3d',
        'total_experience': 'int',
        'velocity': 'Vector3d',
        'world': 'str'
    }

    attribute_map = {
        'damage': 'damage',
        'exhaustion': 'exhaustion',
        'experience_since_level': 'experienceSinceLevel',
        'food_level': 'foodLevel',
        'game_mode': 'gameMode',
        'health': 'health',
        'inventory': 'inventory',
        'level': 'level',
        'max_health': 'maxHealth',
        'position': 'position',
        'rotation': 'rotation',
        'saturation': 'saturation',
        'scale': 'scale',
        'total_experience': 'totalExperience',
        'velocity': 'velocity',
        'world': 'world'
    }

    def __init__(self, damage=None, exhaustion=None, experience_since_level=None, food_level=None, game_mode=None, health=None, inventory=None, level=None, max_health=None, position=None, rotation=None, saturation=None, scale=None, total_experience=None, velocity=None, world=None):  # noqa: E501
        """UpdatePlayerRequest - a model defined in Swagger"""  # noqa: E501

        self._damage = None
        self._exhaustion = None
        self._experience_since_level = None
        self._food_level = None
        self._game_mode = None
        self._health = None
        self._inventory = None
        self._level = None
        self._max_health = None
        self._position = None
        self._rotation = None
        self._saturation = None
        self._scale = None
        self._total_experience = None
        self._velocity = None
        self._world = None
        self.discriminator = None

        if damage is not None:
            self.damage = damage
        if exhaustion is not None:
            self.exhaustion = exhaustion
        if experience_since_level is not None:
            self.experience_since_level = experience_since_level
        if food_level is not None:
            self.food_level = food_level
        if game_mode is not None:
            self.game_mode = game_mode
        if health is not None:
            self.health = health
        if inventory is not None:
            self.inventory = inventory
        if level is not None:
            self.level = level
        if max_health is not None:
            self.max_health = max_health
        if position is not None:
            self.position = position
        if rotation is not None:
            self.rotation = rotation
        if saturation is not None:
            self.saturation = saturation
        if scale is not None:
            self.scale = scale
        if total_experience is not None:
            self.total_experience = total_experience
        if velocity is not None:
            self.velocity = velocity
        if world is not None:
            self.world = world

    @property
    def damage(self):
        """Gets the damage of this UpdatePlayerRequest.  # noqa: E501

        The damage the entity will take  # noqa: E501

        :return: The damage of this UpdatePlayerRequest.  # noqa: E501
        :rtype: DamageRequest
        """
        return self._damage

    @damage.setter
    def damage(self, damage):
        """Sets the damage of this UpdatePlayerRequest.

        The damage the entity will take  # noqa: E501

        :param damage: The damage of this UpdatePlayerRequest.  # noqa: E501
        :type: DamageRequest
        """

        self._damage = damage

    @property
    def exhaustion(self):
        """Gets the exhaustion of this UpdatePlayerRequest.  # noqa: E501

        The exhaustion of the player  # noqa: E501

        :return: The exhaustion of this UpdatePlayerRequest.  # noqa: E501
        :rtype: float
        """
        return self._exhaustion

    @exhaustion.setter
    def exhaustion(self, exhaustion):
        """Sets the exhaustion of this UpdatePlayerRequest.

        The exhaustion of the player  # noqa: E501

        :param exhaustion: The exhaustion of this UpdatePlayerRequest.  # noqa: E501
        :type: float
        """

        self._exhaustion = exhaustion

    @property
    def experience_since_level(self):
        """Gets the experience_since_level of this UpdatePlayerRequest.  # noqa: E501

        The amount of experience gained since the last level  # noqa: E501

        :return: The experience_since_level of this UpdatePlayerRequest.  # noqa: E501
        :rtype: int
        """
        return self._experience_since_level

    @experience_since_level.setter
    def experience_since_level(self, experience_since_level):
        """Sets the experience_since_level of this UpdatePlayerRequest.

        The amount of experience gained since the last level  # noqa: E501

        :param experience_since_level: The experience_since_level of this UpdatePlayerRequest.  # noqa: E501
        :type: int
        """

        self._experience_since_level = experience_since_level

    @property
    def food_level(self):
        """Gets the food_level of this UpdatePlayerRequest.  # noqa: E501

        The food level of the player  # noqa: E501

        :return: The food_level of this UpdatePlayerRequest.  # noqa: E501
        :rtype: int
        """
        return self._food_level

    @food_level.setter
    def food_level(self, food_level):
        """Sets the food_level of this UpdatePlayerRequest.

        The food level of the player  # noqa: E501

        :param food_level: The food_level of this UpdatePlayerRequest.  # noqa: E501
        :type: int
        """

        self._food_level = food_level

    @property
    def game_mode(self):
        """Gets the game_mode of this UpdatePlayerRequest.  # noqa: E501

        The game mode of the player  # noqa: E501

        :return: The game_mode of this UpdatePlayerRequest.  # noqa: E501
        :rtype: str
        """
        return self._game_mode

    @game_mode.setter
    def game_mode(self, game_mode):
        """Sets the game_mode of this UpdatePlayerRequest.

        The game mode of the player  # noqa: E501

        :param game_mode: The game_mode of this UpdatePlayerRequest.  # noqa: E501
        :type: str
        """

        self._game_mode = game_mode

    @property
    def health(self):
        """Gets the health of this UpdatePlayerRequest.  # noqa: E501

        The current amount of health the player has  # noqa: E501

        :return: The health of this UpdatePlayerRequest.  # noqa: E501
        :rtype: float
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this UpdatePlayerRequest.

        The current amount of health the player has  # noqa: E501

        :param health: The health of this UpdatePlayerRequest.  # noqa: E501
        :type: float
        """

        self._health = health

    @property
    def inventory(self):
        """Gets the inventory of this UpdatePlayerRequest.  # noqa: E501

        The slots in the inventory of the entity to modify  # noqa: E501

        :return: The inventory of this UpdatePlayerRequest.  # noqa: E501
        :rtype: list[SlotRequest]
        """
        return self._inventory

    @inventory.setter
    def inventory(self, inventory):
        """Sets the inventory of this UpdatePlayerRequest.

        The slots in the inventory of the entity to modify  # noqa: E501

        :param inventory: The inventory of this UpdatePlayerRequest.  # noqa: E501
        :type: list[SlotRequest]
        """

        self._inventory = inventory

    @property
    def level(self):
        """Gets the level of this UpdatePlayerRequest.  # noqa: E501

        The player level  # noqa: E501

        :return: The level of this UpdatePlayerRequest.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this UpdatePlayerRequest.

        The player level  # noqa: E501

        :param level: The level of this UpdatePlayerRequest.  # noqa: E501
        :type: int
        """

        self._level = level

    @property
    def max_health(self):
        """Gets the max_health of this UpdatePlayerRequest.  # noqa: E501

        The maximum health of the player  # noqa: E501

        :return: The max_health of this UpdatePlayerRequest.  # noqa: E501
        :rtype: float
        """
        return self._max_health

    @max_health.setter
    def max_health(self, max_health):
        """Sets the max_health of this UpdatePlayerRequest.

        The maximum health of the player  # noqa: E501

        :param max_health: The max_health of this UpdatePlayerRequest.  # noqa: E501
        :type: float
        """

        self._max_health = max_health

    @property
    def position(self):
        """Gets the position of this UpdatePlayerRequest.  # noqa: E501

        The position that the entity will be moved to  # noqa: E501

        :return: The position of this UpdatePlayerRequest.  # noqa: E501
        :rtype: Vector3d
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this UpdatePlayerRequest.

        The position that the entity will be moved to  # noqa: E501

        :param position: The position of this UpdatePlayerRequest.  # noqa: E501
        :type: Vector3d
        """

        self._position = position

    @property
    def rotation(self):
        """Gets the rotation of this UpdatePlayerRequest.  # noqa: E501

        The new rotation of the entity  # noqa: E501

        :return: The rotation of this UpdatePlayerRequest.  # noqa: E501
        :rtype: Vector3d
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this UpdatePlayerRequest.

        The new rotation of the entity  # noqa: E501

        :param rotation: The rotation of this UpdatePlayerRequest.  # noqa: E501
        :type: Vector3d
        """

        self._rotation = rotation

    @property
    def saturation(self):
        """Gets the saturation of this UpdatePlayerRequest.  # noqa: E501

        The saturation of the player  # noqa: E501

        :return: The saturation of this UpdatePlayerRequest.  # noqa: E501
        :rtype: float
        """
        return self._saturation

    @saturation.setter
    def saturation(self, saturation):
        """Sets the saturation of this UpdatePlayerRequest.

        The saturation of the player  # noqa: E501

        :param saturation: The saturation of this UpdatePlayerRequest.  # noqa: E501
        :type: float
        """

        self._saturation = saturation

    @property
    def scale(self):
        """Gets the scale of this UpdatePlayerRequest.  # noqa: E501

        The new scale of the entity  # noqa: E501

        :return: The scale of this UpdatePlayerRequest.  # noqa: E501
        :rtype: Vector3d
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this UpdatePlayerRequest.

        The new scale of the entity  # noqa: E501

        :param scale: The scale of this UpdatePlayerRequest.  # noqa: E501
        :type: Vector3d
        """

        self._scale = scale

    @property
    def total_experience(self):
        """Gets the total_experience of this UpdatePlayerRequest.  # noqa: E501

        The total experience of the player  # noqa: E501

        :return: The total_experience of this UpdatePlayerRequest.  # noqa: E501
        :rtype: int
        """
        return self._total_experience

    @total_experience.setter
    def total_experience(self, total_experience):
        """Sets the total_experience of this UpdatePlayerRequest.

        The total experience of the player  # noqa: E501

        :param total_experience: The total_experience of this UpdatePlayerRequest.  # noqa: E501
        :type: int
        """

        self._total_experience = total_experience

    @property
    def velocity(self):
        """Gets the velocity of this UpdatePlayerRequest.  # noqa: E501

        The new speed of the entity  # noqa: E501

        :return: The velocity of this UpdatePlayerRequest.  # noqa: E501
        :rtype: Vector3d
        """
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        """Sets the velocity of this UpdatePlayerRequest.

        The new speed of the entity  # noqa: E501

        :param velocity: The velocity of this UpdatePlayerRequest.  # noqa: E501
        :type: Vector3d
        """

        self._velocity = velocity

    @property
    def world(self):
        """Gets the world of this UpdatePlayerRequest.  # noqa: E501

        The world that the entity will be moved to  # noqa: E501

        :return: The world of this UpdatePlayerRequest.  # noqa: E501
        :rtype: str
        """
        return self._world

    @world.setter
    def world(self, world):
        """Sets the world of this UpdatePlayerRequest.

        The world that the entity will be moved to  # noqa: E501

        :param world: The world of this UpdatePlayerRequest.  # noqa: E501
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
        if issubclass(UpdatePlayerRequest, dict):
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
        if not isinstance(other, UpdatePlayerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
