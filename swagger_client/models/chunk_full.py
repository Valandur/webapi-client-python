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


class ChunkFull(object):
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
        'uuid': 'str',
        'position': 'Vector3',
        'world': 'World',
        'block_min': 'Vector3',
        'block_max': 'Vector3',
        'is_loaded': 'bool',
        'inhabited_time': 'float',
        'difficulty_factor': 'float',
        'difficulty_percentage': 'float'
    }

    attribute_map = {
        'uuid': 'uuid',
        'position': 'position',
        'world': 'world',
        'block_min': 'blockMin',
        'block_max': 'blockMax',
        'is_loaded': 'isLoaded',
        'inhabited_time': 'inhabitedTime',
        'difficulty_factor': 'difficultyFactor',
        'difficulty_percentage': 'difficultyPercentage'
    }

    def __init__(self, uuid=None, position=None, world=None, block_min=None, block_max=None, is_loaded=None, inhabited_time=None, difficulty_factor=None, difficulty_percentage=None):
        """
        ChunkFull - a model defined in Swagger
        """

        self._uuid = None
        self._position = None
        self._world = None
        self._block_min = None
        self._block_max = None
        self._is_loaded = None
        self._inhabited_time = None
        self._difficulty_factor = None
        self._difficulty_percentage = None

        if uuid is not None:
          self.uuid = uuid
        if position is not None:
          self.position = position
        if world is not None:
          self.world = world
        if block_min is not None:
          self.block_min = block_min
        if block_max is not None:
          self.block_max = block_max
        if is_loaded is not None:
          self.is_loaded = is_loaded
        if inhabited_time is not None:
          self.inhabited_time = inhabited_time
        if difficulty_factor is not None:
          self.difficulty_factor = difficulty_factor
        if difficulty_percentage is not None:
          self.difficulty_percentage = difficulty_percentage

    @property
    def uuid(self):
        """
        Gets the uuid of this ChunkFull.
        The unique identifier of the chunk.

        :return: The uuid of this ChunkFull.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this ChunkFull.
        The unique identifier of the chunk.

        :param uuid: The uuid of this ChunkFull.
        :type: str
        """

        self._uuid = uuid

    @property
    def position(self):
        """
        Gets the position of this ChunkFull.

        :return: The position of this ChunkFull.
        :rtype: Vector3
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this ChunkFull.

        :param position: The position of this ChunkFull.
        :type: Vector3
        """

        self._position = position

    @property
    def world(self):
        """
        Gets the world of this ChunkFull.

        :return: The world of this ChunkFull.
        :rtype: World
        """
        return self._world

    @world.setter
    def world(self, world):
        """
        Sets the world of this ChunkFull.

        :param world: The world of this ChunkFull.
        :type: World
        """

        self._world = world

    @property
    def block_min(self):
        """
        Gets the block_min of this ChunkFull.

        :return: The block_min of this ChunkFull.
        :rtype: Vector3
        """
        return self._block_min

    @block_min.setter
    def block_min(self, block_min):
        """
        Sets the block_min of this ChunkFull.

        :param block_min: The block_min of this ChunkFull.
        :type: Vector3
        """

        self._block_min = block_min

    @property
    def block_max(self):
        """
        Gets the block_max of this ChunkFull.

        :return: The block_max of this ChunkFull.
        :rtype: Vector3
        """
        return self._block_max

    @block_max.setter
    def block_max(self, block_max):
        """
        Sets the block_max of this ChunkFull.

        :param block_max: The block_max of this ChunkFull.
        :type: Vector3
        """

        self._block_max = block_max

    @property
    def is_loaded(self):
        """
        Gets the is_loaded of this ChunkFull.
        True if the chunk is currently loaded in the world, false otherwise.

        :return: The is_loaded of this ChunkFull.
        :rtype: bool
        """
        return self._is_loaded

    @is_loaded.setter
    def is_loaded(self, is_loaded):
        """
        Sets the is_loaded of this ChunkFull.
        True if the chunk is currently loaded in the world, false otherwise.

        :param is_loaded: The is_loaded of this ChunkFull.
        :type: bool
        """

        self._is_loaded = is_loaded

    @property
    def inhabited_time(self):
        """
        Gets the inhabited_time of this ChunkFull.
        The number of ticks a player has been present in this chunk.

        :return: The inhabited_time of this ChunkFull.
        :rtype: float
        """
        return self._inhabited_time

    @inhabited_time.setter
    def inhabited_time(self, inhabited_time):
        """
        Sets the inhabited_time of this ChunkFull.
        The number of ticks a player has been present in this chunk.

        :param inhabited_time: The inhabited_time of this ChunkFull.
        :type: float
        """

        self._inhabited_time = inhabited_time

    @property
    def difficulty_factor(self):
        """
        Gets the difficulty_factor of this ChunkFull.
        Gets the regional difficulty factor for this chunk.

        :return: The difficulty_factor of this ChunkFull.
        :rtype: float
        """
        return self._difficulty_factor

    @difficulty_factor.setter
    def difficulty_factor(self, difficulty_factor):
        """
        Sets the difficulty_factor of this ChunkFull.
        Gets the regional difficulty factor for this chunk.

        :param difficulty_factor: The difficulty_factor of this ChunkFull.
        :type: float
        """

        self._difficulty_factor = difficulty_factor

    @property
    def difficulty_percentage(self):
        """
        Gets the difficulty_percentage of this ChunkFull.
        Gets the regional difficulty as a percentage for this chunk.

        :return: The difficulty_percentage of this ChunkFull.
        :rtype: float
        """
        return self._difficulty_percentage

    @difficulty_percentage.setter
    def difficulty_percentage(self, difficulty_percentage):
        """
        Sets the difficulty_percentage of this ChunkFull.
        Gets the regional difficulty as a percentage for this chunk.

        :param difficulty_percentage: The difficulty_percentage of this ChunkFull.
        :type: float
        """

        self._difficulty_percentage = difficulty_percentage

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
        if not isinstance(other, ChunkFull):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
