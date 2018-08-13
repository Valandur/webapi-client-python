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

from swagger_client.models.catalog_type_item_type import CatalogTypeItemType  # noqa: F401,E501


class MMCRestrictItem(object):
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
        'ban_reason': 'str',
        'breaking_banned': 'bool',
        'craft_banned': 'bool',
        'drop_banned': 'bool',
        'item': 'CatalogTypeItemType',
        'link': 'str',
        'ownership_banned': 'bool',
        'placing_banned': 'bool',
        'usage_banned': 'bool',
        'world_banned': 'bool'
    }

    attribute_map = {
        'ban_reason': 'banReason',
        'breaking_banned': 'breakingBanned',
        'craft_banned': 'craftBanned',
        'drop_banned': 'dropBanned',
        'item': 'item',
        'link': 'link',
        'ownership_banned': 'ownershipBanned',
        'placing_banned': 'placingBanned',
        'usage_banned': 'usageBanned',
        'world_banned': 'worldBanned'
    }

    def __init__(self, ban_reason=None, breaking_banned=None, craft_banned=None, drop_banned=None, item=None, link=None, ownership_banned=None, placing_banned=None, usage_banned=None, world_banned=None):  # noqa: E501
        """MMCRestrictItem - a model defined in Swagger"""  # noqa: E501

        self._ban_reason = None
        self._breaking_banned = None
        self._craft_banned = None
        self._drop_banned = None
        self._item = None
        self._link = None
        self._ownership_banned = None
        self._placing_banned = None
        self._usage_banned = None
        self._world_banned = None
        self.discriminator = None

        self.ban_reason = ban_reason
        self.breaking_banned = breaking_banned
        self.craft_banned = craft_banned
        self.drop_banned = drop_banned
        self.item = item
        self.link = link
        self.ownership_banned = ownership_banned
        self.placing_banned = placing_banned
        self.usage_banned = usage_banned
        self.world_banned = world_banned

    @property
    def ban_reason(self):
        """Gets the ban_reason of this MMCRestrictItem.  # noqa: E501

        The reason why the item is banned  # noqa: E501

        :return: The ban_reason of this MMCRestrictItem.  # noqa: E501
        :rtype: str
        """
        return self._ban_reason

    @ban_reason.setter
    def ban_reason(self, ban_reason):
        """Sets the ban_reason of this MMCRestrictItem.

        The reason why the item is banned  # noqa: E501

        :param ban_reason: The ban_reason of this MMCRestrictItem.  # noqa: E501
        :type: str
        """
        if ban_reason is None:
            raise ValueError("Invalid value for `ban_reason`, must not be `None`")  # noqa: E501

        self._ban_reason = ban_reason

    @property
    def breaking_banned(self):
        """Gets the breaking_banned of this MMCRestrictItem.  # noqa: E501

        True if breaking of this item is banned, false otherwise  # noqa: E501

        :return: The breaking_banned of this MMCRestrictItem.  # noqa: E501
        :rtype: bool
        """
        return self._breaking_banned

    @breaking_banned.setter
    def breaking_banned(self, breaking_banned):
        """Sets the breaking_banned of this MMCRestrictItem.

        True if breaking of this item is banned, false otherwise  # noqa: E501

        :param breaking_banned: The breaking_banned of this MMCRestrictItem.  # noqa: E501
        :type: bool
        """
        if breaking_banned is None:
            raise ValueError("Invalid value for `breaking_banned`, must not be `None`")  # noqa: E501

        self._breaking_banned = breaking_banned

    @property
    def craft_banned(self):
        """Gets the craft_banned of this MMCRestrictItem.  # noqa: E501

        True if crafting this item is banned, false otherwise  # noqa: E501

        :return: The craft_banned of this MMCRestrictItem.  # noqa: E501
        :rtype: bool
        """
        return self._craft_banned

    @craft_banned.setter
    def craft_banned(self, craft_banned):
        """Sets the craft_banned of this MMCRestrictItem.

        True if crafting this item is banned, false otherwise  # noqa: E501

        :param craft_banned: The craft_banned of this MMCRestrictItem.  # noqa: E501
        :type: bool
        """
        if craft_banned is None:
            raise ValueError("Invalid value for `craft_banned`, must not be `None`")  # noqa: E501

        self._craft_banned = craft_banned

    @property
    def drop_banned(self):
        """Gets the drop_banned of this MMCRestrictItem.  # noqa: E501

        True if dropping this item is banned, false otherwise  # noqa: E501

        :return: The drop_banned of this MMCRestrictItem.  # noqa: E501
        :rtype: bool
        """
        return self._drop_banned

    @drop_banned.setter
    def drop_banned(self, drop_banned):
        """Sets the drop_banned of this MMCRestrictItem.

        True if dropping this item is banned, false otherwise  # noqa: E501

        :param drop_banned: The drop_banned of this MMCRestrictItem.  # noqa: E501
        :type: bool
        """
        if drop_banned is None:
            raise ValueError("Invalid value for `drop_banned`, must not be `None`")  # noqa: E501

        self._drop_banned = drop_banned

    @property
    def item(self):
        """Gets the item of this MMCRestrictItem.  # noqa: E501

        The item type that is banned  # noqa: E501

        :return: The item of this MMCRestrictItem.  # noqa: E501
        :rtype: CatalogTypeItemType
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this MMCRestrictItem.

        The item type that is banned  # noqa: E501

        :param item: The item of this MMCRestrictItem.  # noqa: E501
        :type: CatalogTypeItemType
        """
        if item is None:
            raise ValueError("Invalid value for `item`, must not be `None`")  # noqa: E501

        self._item = item

    @property
    def link(self):
        """Gets the link of this MMCRestrictItem.  # noqa: E501

        The API link that can be used to obtain more information about this object  # noqa: E501

        :return: The link of this MMCRestrictItem.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this MMCRestrictItem.

        The API link that can be used to obtain more information about this object  # noqa: E501

        :param link: The link of this MMCRestrictItem.  # noqa: E501
        :type: str
        """
        if link is None:
            raise ValueError("Invalid value for `link`, must not be `None`")  # noqa: E501

        self._link = link

    @property
    def ownership_banned(self):
        """Gets the ownership_banned of this MMCRestrictItem.  # noqa: E501

        True if ownership of this item is banned, false otherwise  # noqa: E501

        :return: The ownership_banned of this MMCRestrictItem.  # noqa: E501
        :rtype: bool
        """
        return self._ownership_banned

    @ownership_banned.setter
    def ownership_banned(self, ownership_banned):
        """Sets the ownership_banned of this MMCRestrictItem.

        True if ownership of this item is banned, false otherwise  # noqa: E501

        :param ownership_banned: The ownership_banned of this MMCRestrictItem.  # noqa: E501
        :type: bool
        """
        if ownership_banned is None:
            raise ValueError("Invalid value for `ownership_banned`, must not be `None`")  # noqa: E501

        self._ownership_banned = ownership_banned

    @property
    def placing_banned(self):
        """Gets the placing_banned of this MMCRestrictItem.  # noqa: E501

        True if the placing of this item is banned, false otherwise  # noqa: E501

        :return: The placing_banned of this MMCRestrictItem.  # noqa: E501
        :rtype: bool
        """
        return self._placing_banned

    @placing_banned.setter
    def placing_banned(self, placing_banned):
        """Sets the placing_banned of this MMCRestrictItem.

        True if the placing of this item is banned, false otherwise  # noqa: E501

        :param placing_banned: The placing_banned of this MMCRestrictItem.  # noqa: E501
        :type: bool
        """
        if placing_banned is None:
            raise ValueError("Invalid value for `placing_banned`, must not be `None`")  # noqa: E501

        self._placing_banned = placing_banned

    @property
    def usage_banned(self):
        """Gets the usage_banned of this MMCRestrictItem.  # noqa: E501

        True if the usage of this item is banned, false otherwise  # noqa: E501

        :return: The usage_banned of this MMCRestrictItem.  # noqa: E501
        :rtype: bool
        """
        return self._usage_banned

    @usage_banned.setter
    def usage_banned(self, usage_banned):
        """Sets the usage_banned of this MMCRestrictItem.

        True if the usage of this item is banned, false otherwise  # noqa: E501

        :param usage_banned: The usage_banned of this MMCRestrictItem.  # noqa: E501
        :type: bool
        """
        if usage_banned is None:
            raise ValueError("Invalid value for `usage_banned`, must not be `None`")  # noqa: E501

        self._usage_banned = usage_banned

    @property
    def world_banned(self):
        """Gets the world_banned of this MMCRestrictItem.  # noqa: E501

        True if this item is banned from the world, false otherwise?  # noqa: E501

        :return: The world_banned of this MMCRestrictItem.  # noqa: E501
        :rtype: bool
        """
        return self._world_banned

    @world_banned.setter
    def world_banned(self, world_banned):
        """Sets the world_banned of this MMCRestrictItem.

        True if this item is banned from the world, false otherwise?  # noqa: E501

        :param world_banned: The world_banned of this MMCRestrictItem.  # noqa: E501
        :type: bool
        """
        if world_banned is None:
            raise ValueError("Invalid value for `world_banned`, must not be `None`")  # noqa: E501

        self._world_banned = world_banned

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
        if not isinstance(other, MMCRestrictItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
