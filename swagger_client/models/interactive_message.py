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

from swagger_client.models.interactive_message_option import InteractiveMessageOption  # noqa: F401,E501


class InteractiveMessage(object):
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
        'link': 'str',
        'target': 'str',
        'uuid': 'str',
        'message': 'str',
        'once': 'bool',
        'options': 'list[InteractiveMessageOption]',
        'targets': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'link': 'link',
        'target': 'target',
        'uuid': 'uuid',
        'message': 'message',
        'once': 'once',
        'options': 'options',
        'targets': 'targets'
    }

    def __init__(self, id=None, link=None, target=None, uuid=None, message=None, once=None, options=None, targets=None):  # noqa: E501
        """InteractiveMessage - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._link = None
        self._target = None
        self._uuid = None
        self._message = None
        self._once = None
        self._options = None
        self._targets = None
        self.discriminator = None

        self.id = id
        self.link = link
        self.target = target
        self.uuid = uuid
        if message is not None:
            self.message = message
        if once is not None:
            self.once = once
        if options is not None:
            self.options = options
        if targets is not None:
            self.targets = targets

    @property
    def id(self):
        """Gets the id of this InteractiveMessage.  # noqa: E501

        The id of the message. Used to identify responses.  # noqa: E501

        :return: The id of this InteractiveMessage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InteractiveMessage.

        The id of the message. Used to identify responses.  # noqa: E501

        :param id: The id of this InteractiveMessage.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def link(self):
        """Gets the link of this InteractiveMessage.  # noqa: E501

        The API link that can be used to obtain more information about this object  # noqa: E501

        :return: The link of this InteractiveMessage.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this InteractiveMessage.

        The API link that can be used to obtain more information about this object  # noqa: E501

        :param link: The link of this InteractiveMessage.  # noqa: E501
        :type: str
        """
        if link is None:
            raise ValueError("Invalid value for `link`, must not be `None`")  # noqa: E501

        self._link = link

    @property
    def target(self):
        """Gets the target of this InteractiveMessage.  # noqa: E501

        The target of the message, usually this is a player UUID. Can be set to \"server\" to send to all online players.  # noqa: E501

        :return: The target of this InteractiveMessage.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this InteractiveMessage.

        The target of the message, usually this is a player UUID. Can be set to \"server\" to send to all online players.  # noqa: E501

        :param target: The target of this InteractiveMessage.  # noqa: E501
        :type: str
        """
        if target is None:
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

    @property
    def uuid(self):
        """Gets the uuid of this InteractiveMessage.  # noqa: E501

        The unique UUID of this message  # noqa: E501

        :return: The uuid of this InteractiveMessage.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this InteractiveMessage.

        The unique UUID of this message  # noqa: E501

        :param uuid: The uuid of this InteractiveMessage.  # noqa: E501
        :type: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def message(self):
        """Gets the message of this InteractiveMessage.  # noqa: E501

        The actual content of the message  # noqa: E501

        :return: The message of this InteractiveMessage.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InteractiveMessage.

        The actual content of the message  # noqa: E501

        :param message: The message of this InteractiveMessage.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def once(self):
        """Gets the once of this InteractiveMessage.  # noqa: E501

        True if this message can only be replied to once per target, false otherwise  # noqa: E501

        :return: The once of this InteractiveMessage.  # noqa: E501
        :rtype: bool
        """
        return self._once

    @once.setter
    def once(self, once):
        """Sets the once of this InteractiveMessage.

        True if this message can only be replied to once per target, false otherwise  # noqa: E501

        :param once: The once of this InteractiveMessage.  # noqa: E501
        :type: bool
        """

        self._once = once

    @property
    def options(self):
        """Gets the options of this InteractiveMessage.  # noqa: E501

        Clickable options that the player can select from  # noqa: E501

        :return: The options of this InteractiveMessage.  # noqa: E501
        :rtype: list[InteractiveMessageOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this InteractiveMessage.

        Clickable options that the player can select from  # noqa: E501

        :param options: The options of this InteractiveMessage.  # noqa: E501
        :type: list[InteractiveMessageOption]
        """

        self._options = options

    @property
    def targets(self):
        """Gets the targets of this InteractiveMessage.  # noqa: E501

        A list of targets that will receive the message. Usually a list of player UUIDs  # noqa: E501

        :return: The targets of this InteractiveMessage.  # noqa: E501
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this InteractiveMessage.

        A list of targets that will receive the message. Usually a list of player UUIDs  # noqa: E501

        :param targets: The targets of this InteractiveMessage.  # noqa: E501
        :type: list[str]
        """

        self._targets = targets

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
        if not isinstance(other, InteractiveMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
