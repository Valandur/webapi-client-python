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


class Account(object):
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
        'balances': 'dict(str, float)',
        'display_name': 'str',
        'friendly_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'balances': 'balances',
        'display_name': 'displayName',
        'friendly_id': 'friendlyId',
        'id': 'id'
    }

    def __init__(self, balances=None, display_name=None, friendly_id=None, id=None):  # noqa: E501
        """Account - a model defined in Swagger"""  # noqa: E501

        self._balances = None
        self._display_name = None
        self._friendly_id = None
        self._id = None
        self.discriminator = None

        if balances is not None:
            self.balances = balances
        if display_name is not None:
            self.display_name = display_name
        if friendly_id is not None:
            self.friendly_id = friendly_id
        if id is not None:
            self.id = id

    @property
    def balances(self):
        """Gets the balances of this Account.  # noqa: E501


        :return: The balances of this Account.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._balances

    @balances.setter
    def balances(self, balances):
        """Sets the balances of this Account.


        :param balances: The balances of this Account.  # noqa: E501
        :type: dict(str, float)
        """

        self._balances = balances

    @property
    def display_name(self):
        """Gets the display_name of this Account.  # noqa: E501


        :return: The display_name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Account.


        :param display_name: The display_name of this Account.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def friendly_id(self):
        """Gets the friendly_id of this Account.  # noqa: E501


        :return: The friendly_id of this Account.  # noqa: E501
        :rtype: str
        """
        return self._friendly_id

    @friendly_id.setter
    def friendly_id(self, friendly_id):
        """Sets the friendly_id of this Account.


        :param friendly_id: The friendly_id of this Account.  # noqa: E501
        :type: str
        """

        self._friendly_id = friendly_id

    @property
    def id(self):
        """Gets the id of this Account.  # noqa: E501


        :return: The id of this Account.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Account.


        :param id: The id of this Account.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(Account, dict):
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
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
