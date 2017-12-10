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


class PlayerFull(object):
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
        'type': 'str',
        'uuid': 'str',
        'online': 'bool',
        'location': 'Location',
        'name': 'str',
        'link': 'str',
        '_class': 'str',
        'velocity': 'Vector3',
        'rotation': 'Vector3',
        'scale': 'Vector3',
        'inventory': 'Inventory',
        'connection': 'PlayerFullConnection',
        'armour': 'PlayerFullArmour',
        'achievements': 'list[PlayerFullAchievements]',
        'experience': 'PlayerFullExperience',
        'game_mode': 'str',
        'joined': 'PlayerFullJoined',
        'health': 'PlayerFullHealth',
        'food': 'PlayerFullFood',
        'statistics': 'object'
    }

    attribute_map = {
        'type': 'type',
        'uuid': 'uuid',
        'online': 'online',
        'location': 'location',
        'name': 'name',
        'link': 'link',
        '_class': 'class',
        'velocity': 'velocity',
        'rotation': 'rotation',
        'scale': 'scale',
        'inventory': 'inventory',
        'connection': 'connection',
        'armour': 'armour',
        'achievements': 'achievements',
        'experience': 'experience',
        'game_mode': 'gameMode',
        'joined': 'joined',
        'health': 'health',
        'food': 'food',
        'statistics': 'statistics'
    }

    def __init__(self, type=None, uuid=None, online=None, location=None, name=None, link=None, _class=None, velocity=None, rotation=None, scale=None, inventory=None, connection=None, armour=None, achievements=None, experience=None, game_mode=None, joined=None, health=None, food=None, statistics=None):
        """
        PlayerFull - a model defined in Swagger
        """

        self._type = None
        self._uuid = None
        self._online = None
        self._location = None
        self._name = None
        self._link = None
        self.__class = None
        self._velocity = None
        self._rotation = None
        self._scale = None
        self._inventory = None
        self._connection = None
        self._armour = None
        self._achievements = None
        self._experience = None
        self._game_mode = None
        self._joined = None
        self._health = None
        self._food = None
        self._statistics = None

        if type is not None:
          self.type = type
        if uuid is not None:
          self.uuid = uuid
        if online is not None:
          self.online = online
        if location is not None:
          self.location = location
        if name is not None:
          self.name = name
        if link is not None:
          self.link = link
        if _class is not None:
          self._class = _class
        if velocity is not None:
          self.velocity = velocity
        if rotation is not None:
          self.rotation = rotation
        if scale is not None:
          self.scale = scale
        if inventory is not None:
          self.inventory = inventory
        if connection is not None:
          self.connection = connection
        if armour is not None:
          self.armour = armour
        if achievements is not None:
          self.achievements = achievements
        if experience is not None:
          self.experience = experience
        if game_mode is not None:
          self.game_mode = game_mode
        if joined is not None:
          self.joined = joined
        if health is not None:
          self.health = health
        if food is not None:
          self.food = food
        if statistics is not None:
          self.statistics = statistics

    @property
    def type(self):
        """
        Gets the type of this PlayerFull.
        The type of player, usually `minecraft:player`

        :return: The type of this PlayerFull.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PlayerFull.
        The type of player, usually `minecraft:player`

        :param type: The type of this PlayerFull.
        :type: str
        """

        self._type = type

    @property
    def uuid(self):
        """
        Gets the uuid of this PlayerFull.
        The unique identifier of the player.

        :return: The uuid of this PlayerFull.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this PlayerFull.
        The unique identifier of the player.

        :param uuid: The uuid of this PlayerFull.
        :type: str
        """

        self._uuid = uuid

    @property
    def online(self):
        """
        Gets the online of this PlayerFull.
        True if the player is currently online, false otherwise.

        :return: The online of this PlayerFull.
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """
        Sets the online of this PlayerFull.
        True if the player is currently online, false otherwise.

        :param online: The online of this PlayerFull.
        :type: bool
        """

        self._online = online

    @property
    def location(self):
        """
        Gets the location of this PlayerFull.

        :return: The location of this PlayerFull.
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this PlayerFull.

        :param location: The location of this PlayerFull.
        :type: Location
        """

        self._location = location

    @property
    def name(self):
        """
        Gets the name of this PlayerFull.
        The name of the player.

        :return: The name of this PlayerFull.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PlayerFull.
        The name of the player.

        :param name: The name of this PlayerFull.
        :type: str
        """

        self._name = name

    @property
    def link(self):
        """
        Gets the link of this PlayerFull.
        The API URL which contains detailed information about this player.

        :return: The link of this PlayerFull.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """
        Sets the link of this PlayerFull.
        The API URL which contains detailed information about this player.

        :param link: The link of this PlayerFull.
        :type: str
        """

        self._link = link

    @property
    def _class(self):
        """
        Gets the _class of this PlayerFull.
        The fully qualified class name of the object representing the player. Usually `net.minecraft.entity.player.EntityPlayerMP`.

        :return: The _class of this PlayerFull.
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """
        Sets the _class of this PlayerFull.
        The fully qualified class name of the object representing the player. Usually `net.minecraft.entity.player.EntityPlayerMP`.

        :param _class: The _class of this PlayerFull.
        :type: str
        """

        self.__class = _class

    @property
    def velocity(self):
        """
        Gets the velocity of this PlayerFull.

        :return: The velocity of this PlayerFull.
        :rtype: Vector3
        """
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        """
        Sets the velocity of this PlayerFull.

        :param velocity: The velocity of this PlayerFull.
        :type: Vector3
        """

        self._velocity = velocity

    @property
    def rotation(self):
        """
        Gets the rotation of this PlayerFull.

        :return: The rotation of this PlayerFull.
        :rtype: Vector3
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """
        Sets the rotation of this PlayerFull.

        :param rotation: The rotation of this PlayerFull.
        :type: Vector3
        """

        self._rotation = rotation

    @property
    def scale(self):
        """
        Gets the scale of this PlayerFull.

        :return: The scale of this PlayerFull.
        :rtype: Vector3
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """
        Sets the scale of this PlayerFull.

        :param scale: The scale of this PlayerFull.
        :type: Vector3
        """

        self._scale = scale

    @property
    def inventory(self):
        """
        Gets the inventory of this PlayerFull.

        :return: The inventory of this PlayerFull.
        :rtype: Inventory
        """
        return self._inventory

    @inventory.setter
    def inventory(self, inventory):
        """
        Sets the inventory of this PlayerFull.

        :param inventory: The inventory of this PlayerFull.
        :type: Inventory
        """

        self._inventory = inventory

    @property
    def connection(self):
        """
        Gets the connection of this PlayerFull.

        :return: The connection of this PlayerFull.
        :rtype: PlayerFullConnection
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """
        Sets the connection of this PlayerFull.

        :param connection: The connection of this PlayerFull.
        :type: PlayerFullConnection
        """

        self._connection = connection

    @property
    def armour(self):
        """
        Gets the armour of this PlayerFull.

        :return: The armour of this PlayerFull.
        :rtype: PlayerFullArmour
        """
        return self._armour

    @armour.setter
    def armour(self, armour):
        """
        Sets the armour of this PlayerFull.

        :param armour: The armour of this PlayerFull.
        :type: PlayerFullArmour
        """

        self._armour = armour

    @property
    def achievements(self):
        """
        Gets the achievements of this PlayerFull.
        An array of achievements the player has been awarded.

        :return: The achievements of this PlayerFull.
        :rtype: list[PlayerFullAchievements]
        """
        return self._achievements

    @achievements.setter
    def achievements(self, achievements):
        """
        Sets the achievements of this PlayerFull.
        An array of achievements the player has been awarded.

        :param achievements: The achievements of this PlayerFull.
        :type: list[PlayerFullAchievements]
        """

        self._achievements = achievements

    @property
    def experience(self):
        """
        Gets the experience of this PlayerFull.

        :return: The experience of this PlayerFull.
        :rtype: PlayerFullExperience
        """
        return self._experience

    @experience.setter
    def experience(self, experience):
        """
        Sets the experience of this PlayerFull.

        :param experience: The experience of this PlayerFull.
        :type: PlayerFullExperience
        """

        self._experience = experience

    @property
    def game_mode(self):
        """
        Gets the game_mode of this PlayerFull.
        The current game mode the player is in.

        :return: The game_mode of this PlayerFull.
        :rtype: str
        """
        return self._game_mode

    @game_mode.setter
    def game_mode(self, game_mode):
        """
        Sets the game_mode of this PlayerFull.
        The current game mode the player is in.

        :param game_mode: The game_mode of this PlayerFull.
        :type: str
        """

        self._game_mode = game_mode

    @property
    def joined(self):
        """
        Gets the joined of this PlayerFull.

        :return: The joined of this PlayerFull.
        :rtype: PlayerFullJoined
        """
        return self._joined

    @joined.setter
    def joined(self, joined):
        """
        Sets the joined of this PlayerFull.

        :param joined: The joined of this PlayerFull.
        :type: PlayerFullJoined
        """

        self._joined = joined

    @property
    def health(self):
        """
        Gets the health of this PlayerFull.

        :return: The health of this PlayerFull.
        :rtype: PlayerFullHealth
        """
        return self._health

    @health.setter
    def health(self, health):
        """
        Sets the health of this PlayerFull.

        :param health: The health of this PlayerFull.
        :type: PlayerFullHealth
        """

        self._health = health

    @property
    def food(self):
        """
        Gets the food of this PlayerFull.

        :return: The food of this PlayerFull.
        :rtype: PlayerFullFood
        """
        return self._food

    @food.setter
    def food(self, food):
        """
        Sets the food of this PlayerFull.

        :param food: The food of this PlayerFull.
        :type: PlayerFullFood
        """

        self._food = food

    @property
    def statistics(self):
        """
        Gets the statistics of this PlayerFull.
        A map from statistics id to value, keeping track of the players actions.

        :return: The statistics of this PlayerFull.
        :rtype: object
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """
        Sets the statistics of this PlayerFull.
        A map from statistics id to value, keeping track of the players actions.

        :param statistics: The statistics of this PlayerFull.
        :type: object
        """

        self._statistics = statistics

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
        if not isinstance(other, PlayerFull):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
