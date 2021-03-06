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


class FurnaceData(object):
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
        'max_burn_time': 'int',
        'max_cook_time': 'int',
        'passed_burn_time': 'int',
        'passed_cook_time': 'int'
    }

    attribute_map = {
        'max_burn_time': 'maxBurnTime',
        'max_cook_time': 'maxCookTime',
        'passed_burn_time': 'passedBurnTime',
        'passed_cook_time': 'passedCookTime'
    }

    def __init__(self, max_burn_time=None, max_cook_time=None, passed_burn_time=None, passed_cook_time=None):  # noqa: E501
        """FurnaceData - a model defined in Swagger"""  # noqa: E501

        self._max_burn_time = None
        self._max_cook_time = None
        self._passed_burn_time = None
        self._passed_cook_time = None
        self.discriminator = None

        self.max_burn_time = max_burn_time
        self.max_cook_time = max_cook_time
        self.passed_burn_time = passed_burn_time
        self.passed_cook_time = passed_cook_time

    @property
    def max_burn_time(self):
        """Gets the max_burn_time of this FurnaceData.  # noqa: E501

        The maximum amount of time (in ticks) the current fuel item lasts  # noqa: E501

        :return: The max_burn_time of this FurnaceData.  # noqa: E501
        :rtype: int
        """
        return self._max_burn_time

    @max_burn_time.setter
    def max_burn_time(self, max_burn_time):
        """Sets the max_burn_time of this FurnaceData.

        The maximum amount of time (in ticks) the current fuel item lasts  # noqa: E501

        :param max_burn_time: The max_burn_time of this FurnaceData.  # noqa: E501
        :type: int
        """
        if max_burn_time is None:
            raise ValueError("Invalid value for `max_burn_time`, must not be `None`")  # noqa: E501

        self._max_burn_time = max_burn_time

    @property
    def max_cook_time(self):
        """Gets the max_cook_time of this FurnaceData.  # noqa: E501

        The total amount of time (in ticks) the stack has to cook for to be done  # noqa: E501

        :return: The max_cook_time of this FurnaceData.  # noqa: E501
        :rtype: int
        """
        return self._max_cook_time

    @max_cook_time.setter
    def max_cook_time(self, max_cook_time):
        """Sets the max_cook_time of this FurnaceData.

        The total amount of time (in ticks) the stack has to cook for to be done  # noqa: E501

        :param max_cook_time: The max_cook_time of this FurnaceData.  # noqa: E501
        :type: int
        """
        if max_cook_time is None:
            raise ValueError("Invalid value for `max_cook_time`, must not be `None`")  # noqa: E501

        self._max_cook_time = max_cook_time

    @property
    def passed_burn_time(self):
        """Gets the passed_burn_time of this FurnaceData.  # noqa: E501

        The amount of time (in ticks) that has passed since this fuel item started burning  # noqa: E501

        :return: The passed_burn_time of this FurnaceData.  # noqa: E501
        :rtype: int
        """
        return self._passed_burn_time

    @passed_burn_time.setter
    def passed_burn_time(self, passed_burn_time):
        """Sets the passed_burn_time of this FurnaceData.

        The amount of time (in ticks) that has passed since this fuel item started burning  # noqa: E501

        :param passed_burn_time: The passed_burn_time of this FurnaceData.  # noqa: E501
        :type: int
        """
        if passed_burn_time is None:
            raise ValueError("Invalid value for `passed_burn_time`, must not be `None`")  # noqa: E501

        self._passed_burn_time = passed_burn_time

    @property
    def passed_cook_time(self):
        """Gets the passed_cook_time of this FurnaceData.  # noqa: E501

        The amount of time (in ticks) that has passed since the item stack started cooking  # noqa: E501

        :return: The passed_cook_time of this FurnaceData.  # noqa: E501
        :rtype: int
        """
        return self._passed_cook_time

    @passed_cook_time.setter
    def passed_cook_time(self, passed_cook_time):
        """Sets the passed_cook_time of this FurnaceData.

        The amount of time (in ticks) that has passed since the item stack started cooking  # noqa: E501

        :param passed_cook_time: The passed_cook_time of this FurnaceData.  # noqa: E501
        :type: int
        """
        if passed_cook_time is None:
            raise ValueError("Invalid value for `passed_cook_time`, must not be `None`")  # noqa: E501

        self._passed_cook_time = passed_cook_time

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
        if issubclass(FurnaceData, dict):
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
        if not isinstance(other, FurnaceData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
