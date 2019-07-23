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


class ExecuteCommandRequest(object):
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
        'command': 'str',
        'hidden_in_console': 'bool',
        'name': 'str',
        'wait_lines': 'int',
        'wait_time': 'int'
    }

    attribute_map = {
        'command': 'command',
        'hidden_in_console': 'hiddenInConsole',
        'name': 'name',
        'wait_lines': 'waitLines',
        'wait_time': 'waitTime'
    }

    def __init__(self, command=None, hidden_in_console=None, name=None, wait_lines=None, wait_time=None):  # noqa: E501
        """ExecuteCommandRequest - a model defined in Swagger"""  # noqa: E501

        self._command = None
        self._hidden_in_console = None
        self._name = None
        self._wait_lines = None
        self._wait_time = None
        self.discriminator = None

        self.command = command
        if hidden_in_console is not None:
            self.hidden_in_console = hidden_in_console
        if name is not None:
            self.name = name
        if wait_lines is not None:
            self.wait_lines = wait_lines
        if wait_time is not None:
            self.wait_time = wait_time

    @property
    def command(self):
        """Gets the command of this ExecuteCommandRequest.  # noqa: E501

        The command to execute  # noqa: E501

        :return: The command of this ExecuteCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this ExecuteCommandRequest.

        The command to execute  # noqa: E501

        :param command: The command of this ExecuteCommandRequest.  # noqa: E501
        :type: str
        """
        if command is None:
            raise ValueError("Invalid value for `command`, must not be `None`")  # noqa: E501

        self._command = command

    @property
    def hidden_in_console(self):
        """Gets the hidden_in_console of this ExecuteCommandRequest.  # noqa: E501

        True to hide the execution of the command in the console, false otherwise  # noqa: E501

        :return: The hidden_in_console of this ExecuteCommandRequest.  # noqa: E501
        :rtype: bool
        """
        return self._hidden_in_console

    @hidden_in_console.setter
    def hidden_in_console(self, hidden_in_console):
        """Sets the hidden_in_console of this ExecuteCommandRequest.

        True to hide the execution of the command in the console, false otherwise  # noqa: E501

        :param hidden_in_console: The hidden_in_console of this ExecuteCommandRequest.  # noqa: E501
        :type: bool
        """

        self._hidden_in_console = hidden_in_console

    @property
    def name(self):
        """Gets the name of this ExecuteCommandRequest.  # noqa: E501

        The name of the source that executes the command  # noqa: E501

        :return: The name of this ExecuteCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExecuteCommandRequest.

        The name of the source that executes the command  # noqa: E501

        :param name: The name of this ExecuteCommandRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def wait_lines(self):
        """Gets the wait_lines of this ExecuteCommandRequest.  # noqa: E501

        The amount of text lines to wait for in the response  # noqa: E501

        :return: The wait_lines of this ExecuteCommandRequest.  # noqa: E501
        :rtype: int
        """
        return self._wait_lines

    @wait_lines.setter
    def wait_lines(self, wait_lines):
        """Sets the wait_lines of this ExecuteCommandRequest.

        The amount of text lines to wait for in the response  # noqa: E501

        :param wait_lines: The wait_lines of this ExecuteCommandRequest.  # noqa: E501
        :type: int
        """

        self._wait_lines = wait_lines

    @property
    def wait_time(self):
        """Gets the wait_time of this ExecuteCommandRequest.  # noqa: E501

        The amount of time to wait for a response  # noqa: E501

        :return: The wait_time of this ExecuteCommandRequest.  # noqa: E501
        :rtype: int
        """
        return self._wait_time

    @wait_time.setter
    def wait_time(self, wait_time):
        """Sets the wait_time of this ExecuteCommandRequest.

        The amount of time to wait for a response  # noqa: E501

        :param wait_time: The wait_time of this ExecuteCommandRequest.  # noqa: E501
        :type: int
        """

        self._wait_time = wait_time

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
        if issubclass(ExecuteCommandRequest, dict):
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
        if not isinstance(other, ExecuteCommandRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
