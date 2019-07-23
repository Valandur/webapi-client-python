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


class CommandData(object):
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
        'tracks_output': 'bool',
        'last_output': 'str',
        'stored_command': 'str',
        'success_count': 'int'
    }

    attribute_map = {
        'tracks_output': 'tracksOutput',
        'last_output': 'lastOutput',
        'stored_command': 'storedCommand',
        'success_count': 'successCount'
    }

    def __init__(self, tracks_output=None, last_output=None, stored_command=None, success_count=None):  # noqa: E501
        """CommandData - a model defined in Swagger"""  # noqa: E501

        self._tracks_output = None
        self._last_output = None
        self._stored_command = None
        self._success_count = None
        self.discriminator = None

        self.tracks_output = tracks_output
        if last_output is not None:
            self.last_output = last_output
        self.stored_command = stored_command
        self.success_count = success_count

    @property
    def tracks_output(self):
        """Gets the tracks_output of this CommandData.  # noqa: E501

        True if the output is tracked, false otherwise  # noqa: E501

        :return: The tracks_output of this CommandData.  # noqa: E501
        :rtype: bool
        """
        return self._tracks_output

    @tracks_output.setter
    def tracks_output(self, tracks_output):
        """Sets the tracks_output of this CommandData.

        True if the output is tracked, false otherwise  # noqa: E501

        :param tracks_output: The tracks_output of this CommandData.  # noqa: E501
        :type: bool
        """
        if tracks_output is None:
            raise ValueError("Invalid value for `tracks_output`, must not be `None`")  # noqa: E501

        self._tracks_output = tracks_output

    @property
    def last_output(self):
        """Gets the last_output of this CommandData.  # noqa: E501

        The last output produced  # noqa: E501

        :return: The last_output of this CommandData.  # noqa: E501
        :rtype: str
        """
        return self._last_output

    @last_output.setter
    def last_output(self, last_output):
        """Sets the last_output of this CommandData.

        The last output produced  # noqa: E501

        :param last_output: The last_output of this CommandData.  # noqa: E501
        :type: str
        """

        self._last_output = last_output

    @property
    def stored_command(self):
        """Gets the stored_command of this CommandData.  # noqa: E501

        The stored command  # noqa: E501

        :return: The stored_command of this CommandData.  # noqa: E501
        :rtype: str
        """
        return self._stored_command

    @stored_command.setter
    def stored_command(self, stored_command):
        """Sets the stored_command of this CommandData.

        The stored command  # noqa: E501

        :param stored_command: The stored_command of this CommandData.  # noqa: E501
        :type: str
        """
        if stored_command is None:
            raise ValueError("Invalid value for `stored_command`, must not be `None`")  # noqa: E501

        self._stored_command = stored_command

    @property
    def success_count(self):
        """Gets the success_count of this CommandData.  # noqa: E501

        The amount of successfull executions  # noqa: E501

        :return: The success_count of this CommandData.  # noqa: E501
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        """Sets the success_count of this CommandData.

        The amount of successfull executions  # noqa: E501

        :param success_count: The success_count of this CommandData.  # noqa: E501
        :type: int
        """
        if success_count is None:
            raise ValueError("Invalid value for `success_count`, must not be `None`")  # noqa: E501

        self._success_count = success_count

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
        if issubclass(CommandData, dict):
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
        if not isinstance(other, CommandData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
