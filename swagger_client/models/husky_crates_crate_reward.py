# coding: utf-8

"""
    Web-API

    Access Sponge powered Minecraft servers through a WebAPI  # Introduction This is the documentation of the various API routes offered by the WebAPI plugin.  This documentation assumes that you are familiar with the basic concepts of Web API's, such as `GET`, `PUT`, `POST` and `DELETE` methods, request `HEADERS` and `RESPONSE CODES` and `JSON` data.  By default this documentation can be found at http:/localhost:8080 (while your minecraft server is running) and the various routes start with http:/localhost:8080/api/v5...  As a quick test try reaching the route http:/localhost:8080/api/v5/info (remember that you can only access \\\"localhost\\\" routes on the server on which you are running minecraft). This route should show you basic information about your server, like the motd and player count.  # List endpoints Lots of objects offer an endpoint to list all objects (e.g. `GET: /world` to get all worlds). These endpoints return only the properties marked 'required' by default, because the list might be quite large. If you want to return ALL data for a list endpoint add the query parameter `details`, (e.g. `GET: /world?details`).  > Remember that in this case the data returned by the endpoint might be quite large.  # Debugging endpoints Apart from the `?details` flag you can also pass some other flags for debugging purposes. Remember that you must include the first query parameter with `?`, and further ones with `&`:  `details`: Includes details for list endpoints  `accept=[json/xml]`: Manually set the accept content type. This is good for browser testing, **BUT DON'T USE THIS IN PRODUCTION, YOU CAN SUPPLY THE `Accepts` HEADER FOR THAT**  `pretty`: Pretty prints the data, also good for debugging in the browser.  An example request might look like this: `http://localhost:8080/api/v5/world?details&accpet=json&pretty&key=MY-API-KEY`  # Additional data Certain endpoints (such as `/player`, `/entity` and `/tile-entity` have additional properties which are not documented here, because the data depends on the concrete object type (eg. `Sheep` have a wool color, others do not) and on the other plugins/mods that are running on your server which might add additional data.  You can also find more information in the github docs (https:/github.com/Valandur/Web-API/tree/master/docs/DATA.md)  # noqa: E501

    OpenAPI spec version: @version@
    Contact: inithilian@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.husky_crates_crate_reward_object import HuskyCratesCrateRewardObject  # noqa: F401,E501
from swagger_client.models.item_stack import ItemStack  # noqa: F401,E501


class HuskyCratesCrateReward(object):
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
        'announce': 'bool',
        'chance': 'float',
        'display_item': 'ItemStack',
        'name': 'str',
        'objects': 'list[HuskyCratesCrateRewardObject]'
    }

    attribute_map = {
        'announce': 'announce',
        'chance': 'chance',
        'display_item': 'displayItem',
        'name': 'name',
        'objects': 'objects'
    }

    def __init__(self, announce=None, chance=None, display_item=None, name=None, objects=None):  # noqa: E501
        """HuskyCratesCrateReward - a model defined in Swagger"""  # noqa: E501

        self._announce = None
        self._chance = None
        self._display_item = None
        self._name = None
        self._objects = None
        self.discriminator = None

        self.announce = announce
        self.chance = chance
        self.display_item = display_item
        self.name = name
        self.objects = objects

    @property
    def announce(self):
        """Gets the announce of this HuskyCratesCrateReward.  # noqa: E501

        True if this reward is announced in chat, false otherwise  # noqa: E501

        :return: The announce of this HuskyCratesCrateReward.  # noqa: E501
        :rtype: bool
        """
        return self._announce

    @announce.setter
    def announce(self, announce):
        """Sets the announce of this HuskyCratesCrateReward.

        True if this reward is announced in chat, false otherwise  # noqa: E501

        :param announce: The announce of this HuskyCratesCrateReward.  # noqa: E501
        :type: bool
        """
        if announce is None:
            raise ValueError("Invalid value for `announce`, must not be `None`")  # noqa: E501

        self._announce = announce

    @property
    def chance(self):
        """Gets the chance of this HuskyCratesCrateReward.  # noqa: E501

        The chance to aquire this reward. This is relative to the chances of the other rewards in this crate  # noqa: E501

        :return: The chance of this HuskyCratesCrateReward.  # noqa: E501
        :rtype: float
        """
        return self._chance

    @chance.setter
    def chance(self, chance):
        """Sets the chance of this HuskyCratesCrateReward.

        The chance to aquire this reward. This is relative to the chances of the other rewards in this crate  # noqa: E501

        :param chance: The chance of this HuskyCratesCrateReward.  # noqa: E501
        :type: float
        """
        if chance is None:
            raise ValueError("Invalid value for `chance`, must not be `None`")  # noqa: E501

        self._chance = chance

    @property
    def display_item(self):
        """Gets the display_item of this HuskyCratesCrateReward.  # noqa: E501

        The ItemStack that is shown in the UI  # noqa: E501

        :return: The display_item of this HuskyCratesCrateReward.  # noqa: E501
        :rtype: ItemStack
        """
        return self._display_item

    @display_item.setter
    def display_item(self, display_item):
        """Sets the display_item of this HuskyCratesCrateReward.

        The ItemStack that is shown in the UI  # noqa: E501

        :param display_item: The display_item of this HuskyCratesCrateReward.  # noqa: E501
        :type: ItemStack
        """
        if display_item is None:
            raise ValueError("Invalid value for `display_item`, must not be `None`")  # noqa: E501

        self._display_item = display_item

    @property
    def name(self):
        """Gets the name of this HuskyCratesCrateReward.  # noqa: E501

        The name of this reward  # noqa: E501

        :return: The name of this HuskyCratesCrateReward.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HuskyCratesCrateReward.

        The name of this reward  # noqa: E501

        :param name: The name of this HuskyCratesCrateReward.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def objects(self):
        """Gets the objects of this HuskyCratesCrateReward.  # noqa: E501

        The objects that are rewarded as part of this reward (can be commands and/or items)  # noqa: E501

        :return: The objects of this HuskyCratesCrateReward.  # noqa: E501
        :rtype: list[HuskyCratesCrateRewardObject]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """Sets the objects of this HuskyCratesCrateReward.

        The objects that are rewarded as part of this reward (can be commands and/or items)  # noqa: E501

        :param objects: The objects of this HuskyCratesCrateReward.  # noqa: E501
        :type: list[HuskyCratesCrateRewardObject]
        """
        if objects is None:
            raise ValueError("Invalid value for `objects`, must not be `None`")  # noqa: E501

        self._objects = objects

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
        if not isinstance(other, HuskyCratesCrateReward):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
