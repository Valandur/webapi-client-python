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

from swagger_client.models.advancement import Advancement  # noqa: F401,E501
from swagger_client.models.catalog_type_advancement_tree import CatalogTypeAdvancementTree  # noqa: F401,E501


class Advancement(object):
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
        'id': 'str',
        'name': 'str',
        'title': 'str',
        'announce_to_chat': 'bool',
        'description': 'str',
        'hidden': 'bool',
        'parent': 'Advancement',
        'show_toast': 'bool',
        'tree': 'CatalogTypeAdvancementTree'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'title': 'title',
        'announce_to_chat': 'announceToChat',
        'description': 'description',
        'hidden': 'hidden',
        'parent': 'parent',
        'show_toast': 'showToast',
        'tree': 'tree'
    }

    def __init__(self, id=None, name=None, title=None, announce_to_chat=None, description=None, hidden=None, parent=None, show_toast=None, tree=None):  # noqa: E501
        """Advancement - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._title = None
        self._announce_to_chat = None
        self._description = None
        self._hidden = None
        self._parent = None
        self._show_toast = None
        self._tree = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.title = title
        if announce_to_chat is not None:
            self.announce_to_chat = announce_to_chat
        if description is not None:
            self.description = description
        if hidden is not None:
            self.hidden = hidden
        if parent is not None:
            self.parent = parent
        if show_toast is not None:
            self.show_toast = show_toast
        if tree is not None:
            self.tree = tree

    @property
    def id(self):
        """Gets the id of this Advancement.  # noqa: E501

        The unique id of the advancement  # noqa: E501

        :return: The id of this Advancement.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Advancement.

        The unique id of the advancement  # noqa: E501

        :param id: The id of this Advancement.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Advancement.  # noqa: E501

        The name of the advancement  # noqa: E501

        :return: The name of this Advancement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Advancement.

        The name of the advancement  # noqa: E501

        :param name: The name of this Advancement.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def title(self):
        """Gets the title of this Advancement.  # noqa: E501

        The title of the advancement  # noqa: E501

        :return: The title of this Advancement.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Advancement.

        The title of the advancement  # noqa: E501

        :param title: The title of this Advancement.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def announce_to_chat(self):
        """Gets the announce_to_chat of this Advancement.  # noqa: E501

        True if the achieving of this advancement is announced in chat, false otherwise  # noqa: E501

        :return: The announce_to_chat of this Advancement.  # noqa: E501
        :rtype: bool
        """
        return self._announce_to_chat

    @announce_to_chat.setter
    def announce_to_chat(self, announce_to_chat):
        """Sets the announce_to_chat of this Advancement.

        True if the achieving of this advancement is announced in chat, false otherwise  # noqa: E501

        :param announce_to_chat: The announce_to_chat of this Advancement.  # noqa: E501
        :type: bool
        """

        self._announce_to_chat = announce_to_chat

    @property
    def description(self):
        """Gets the description of this Advancement.  # noqa: E501

        The description of the advancement  # noqa: E501

        :return: The description of this Advancement.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Advancement.

        The description of the advancement  # noqa: E501

        :param description: The description of this Advancement.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hidden(self):
        """Gets the hidden of this Advancement.  # noqa: E501

        True if this is a hidden advancement  # noqa: E501

        :return: The hidden of this Advancement.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this Advancement.

        True if this is a hidden advancement  # noqa: E501

        :param hidden: The hidden of this Advancement.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def parent(self):
        """Gets the parent of this Advancement.  # noqa: E501

        The parent advancement, which must be unlocked prior to this advancement  # noqa: E501

        :return: The parent of this Advancement.  # noqa: E501
        :rtype: Advancement
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this Advancement.

        The parent advancement, which must be unlocked prior to this advancement  # noqa: E501

        :param parent: The parent of this Advancement.  # noqa: E501
        :type: Advancement
        """

        self._parent = parent

    @property
    def show_toast(self):
        """Gets the show_toast of this Advancement.  # noqa: E501

        True if achieving this advancement shows the player a toast message, false otherwise  # noqa: E501

        :return: The show_toast of this Advancement.  # noqa: E501
        :rtype: bool
        """
        return self._show_toast

    @show_toast.setter
    def show_toast(self, show_toast):
        """Sets the show_toast of this Advancement.

        True if achieving this advancement shows the player a toast message, false otherwise  # noqa: E501

        :param show_toast: The show_toast of this Advancement.  # noqa: E501
        :type: bool
        """

        self._show_toast = show_toast

    @property
    def tree(self):
        """Gets the tree of this Advancement.  # noqa: E501

        The advancement tree that this advancement belongs to  # noqa: E501

        :return: The tree of this Advancement.  # noqa: E501
        :rtype: CatalogTypeAdvancementTree
        """
        return self._tree

    @tree.setter
    def tree(self, tree):
        """Sets the tree of this Advancement.

        The advancement tree that this advancement belongs to  # noqa: E501

        :param tree: The tree of this Advancement.  # noqa: E501
        :type: CatalogTypeAdvancementTree
        """

        self._tree = tree

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
        if not isinstance(other, Advancement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
