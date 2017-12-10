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


class NationsNationFull(object):
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
        'name': 'str',
        'tag': 'str',
        'president': 'Player',
        'real_name': 'str',
        'upkeep': 'float',
        'taxes': 'float',
        'flags': 'object',
        'citizens': 'list[Player]',
        'ministers': 'list[Player]',
        'staff': 'list[Player]',
        'spawns': 'object',
        'rects': 'list[NationsRect]',
        'zones': 'list[NationsZone]'
    }

    attribute_map = {
        'uuid': 'uuid',
        'name': 'name',
        'tag': 'tag',
        'president': 'president',
        'real_name': 'realName',
        'upkeep': 'upkeep',
        'taxes': 'taxes',
        'flags': 'flags',
        'citizens': 'citizens',
        'ministers': 'ministers',
        'staff': 'staff',
        'spawns': 'spawns',
        'rects': 'rects',
        'zones': 'zones'
    }

    def __init__(self, uuid=None, name=None, tag=None, president=None, real_name=None, upkeep=None, taxes=None, flags=None, citizens=None, ministers=None, staff=None, spawns=None, rects=None, zones=None):
        """
        NationsNationFull - a model defined in Swagger
        """

        self._uuid = None
        self._name = None
        self._tag = None
        self._president = None
        self._real_name = None
        self._upkeep = None
        self._taxes = None
        self._flags = None
        self._citizens = None
        self._ministers = None
        self._staff = None
        self._spawns = None
        self._rects = None
        self._zones = None

        if uuid is not None:
          self.uuid = uuid
        if name is not None:
          self.name = name
        if tag is not None:
          self.tag = tag
        if president is not None:
          self.president = president
        if real_name is not None:
          self.real_name = real_name
        if upkeep is not None:
          self.upkeep = upkeep
        if taxes is not None:
          self.taxes = taxes
        if flags is not None:
          self.flags = flags
        if citizens is not None:
          self.citizens = citizens
        if ministers is not None:
          self.ministers = ministers
        if staff is not None:
          self.staff = staff
        if spawns is not None:
          self.spawns = spawns
        if rects is not None:
          self.rects = rects
        if zones is not None:
          self.zones = zones

    @property
    def uuid(self):
        """
        Gets the uuid of this NationsNationFull.
        The unique id of the nation.

        :return: The uuid of this NationsNationFull.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this NationsNationFull.
        The unique id of the nation.

        :param uuid: The uuid of this NationsNationFull.
        :type: str
        """

        self._uuid = uuid

    @property
    def name(self):
        """
        Gets the name of this NationsNationFull.
        The name of the nation.

        :return: The name of this NationsNationFull.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NationsNationFull.
        The name of the nation.

        :param name: The name of this NationsNationFull.
        :type: str
        """

        self._name = name

    @property
    def tag(self):
        """
        Gets the tag of this NationsNationFull.
        The tag of the nation.

        :return: The tag of this NationsNationFull.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this NationsNationFull.
        The tag of the nation.

        :param tag: The tag of this NationsNationFull.
        :type: str
        """

        self._tag = tag

    @property
    def president(self):
        """
        Gets the president of this NationsNationFull.

        :return: The president of this NationsNationFull.
        :rtype: Player
        """
        return self._president

    @president.setter
    def president(self, president):
        """
        Sets the president of this NationsNationFull.

        :param president: The president of this NationsNationFull.
        :type: Player
        """

        self._president = president

    @property
    def real_name(self):
        """
        Gets the real_name of this NationsNationFull.
        The real name of the nation.

        :return: The real_name of this NationsNationFull.
        :rtype: str
        """
        return self._real_name

    @real_name.setter
    def real_name(self, real_name):
        """
        Sets the real_name of this NationsNationFull.
        The real name of the nation.

        :param real_name: The real_name of this NationsNationFull.
        :type: str
        """

        self._real_name = real_name

    @property
    def upkeep(self):
        """
        Gets the upkeep of this NationsNationFull.
        How much upkeep has to be paid for this nation.

        :return: The upkeep of this NationsNationFull.
        :rtype: float
        """
        return self._upkeep

    @upkeep.setter
    def upkeep(self, upkeep):
        """
        Sets the upkeep of this NationsNationFull.
        How much upkeep has to be paid for this nation.

        :param upkeep: The upkeep of this NationsNationFull.
        :type: float
        """

        self._upkeep = upkeep

    @property
    def taxes(self):
        """
        Gets the taxes of this NationsNationFull.
        The amount of taxes that citizens are charged.

        :return: The taxes of this NationsNationFull.
        :rtype: float
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """
        Sets the taxes of this NationsNationFull.
        The amount of taxes that citizens are charged.

        :param taxes: The taxes of this NationsNationFull.
        :type: float
        """

        self._taxes = taxes

    @property
    def flags(self):
        """
        Gets the flags of this NationsNationFull.
        A map of flags

        :return: The flags of this NationsNationFull.
        :rtype: object
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """
        Sets the flags of this NationsNationFull.
        A map of flags

        :param flags: The flags of this NationsNationFull.
        :type: object
        """

        self._flags = flags

    @property
    def citizens(self):
        """
        Gets the citizens of this NationsNationFull.
        The citizens that belong to this nation.

        :return: The citizens of this NationsNationFull.
        :rtype: list[Player]
        """
        return self._citizens

    @citizens.setter
    def citizens(self, citizens):
        """
        Sets the citizens of this NationsNationFull.
        The citizens that belong to this nation.

        :param citizens: The citizens of this NationsNationFull.
        :type: list[Player]
        """

        self._citizens = citizens

    @property
    def ministers(self):
        """
        Gets the ministers of this NationsNationFull.
        The ministers that belong to this nation.

        :return: The ministers of this NationsNationFull.
        :rtype: list[Player]
        """
        return self._ministers

    @ministers.setter
    def ministers(self, ministers):
        """
        Sets the ministers of this NationsNationFull.
        The ministers that belong to this nation.

        :param ministers: The ministers of this NationsNationFull.
        :type: list[Player]
        """

        self._ministers = ministers

    @property
    def staff(self):
        """
        Gets the staff of this NationsNationFull.
        The staff that belong to this nation.

        :return: The staff of this NationsNationFull.
        :rtype: list[Player]
        """
        return self._staff

    @staff.setter
    def staff(self, staff):
        """
        Sets the staff of this NationsNationFull.
        The staff that belong to this nation.

        :param staff: The staff of this NationsNationFull.
        :type: list[Player]
        """

        self._staff = staff

    @property
    def spawns(self):
        """
        Gets the spawns of this NationsNationFull.
        A map of spawn names to spawn locations.

        :return: The spawns of this NationsNationFull.
        :rtype: object
        """
        return self._spawns

    @spawns.setter
    def spawns(self, spawns):
        """
        Sets the spawns of this NationsNationFull.
        A map of spawn names to spawn locations.

        :param spawns: The spawns of this NationsNationFull.
        :type: object
        """

        self._spawns = spawns

    @property
    def rects(self):
        """
        Gets the rects of this NationsNationFull.
        The rects that define the area of this nation.

        :return: The rects of this NationsNationFull.
        :rtype: list[NationsRect]
        """
        return self._rects

    @rects.setter
    def rects(self, rects):
        """
        Sets the rects of this NationsNationFull.
        The rects that define the area of this nation.

        :param rects: The rects of this NationsNationFull.
        :type: list[NationsRect]
        """

        self._rects = rects

    @property
    def zones(self):
        """
        Gets the zones of this NationsNationFull.
        The zones that belong to this nation.

        :return: The zones of this NationsNationFull.
        :rtype: list[NationsZone]
        """
        return self._zones

    @zones.setter
    def zones(self, zones):
        """
        Sets the zones of this NationsNationFull.
        The zones that belong to this nation.

        :param zones: The zones of this NationsNationFull.
        :type: list[NationsZone]
        """

        self._zones = zones

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
        if not isinstance(other, NationsNationFull):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
