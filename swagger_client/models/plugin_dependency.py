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


class PluginDependency(object):
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
        'load_order': 'str',
        'optional': 'bool',
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'load_order': 'loadOrder',
        'optional': 'optional',
        'version': 'version'
    }

    def __init__(self, id=None, load_order=None, optional=None, version=None):  # noqa: E501
        """PluginDependency - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._load_order = None
        self._optional = None
        self._version = None
        self.discriminator = None

        self.id = id
        self.load_order = load_order
        self.optional = optional
        self.version = version

    @property
    def id(self):
        """Gets the id of this PluginDependency.  # noqa: E501

        The id of the plugin that the original plugin depends on  # noqa: E501

        :return: The id of this PluginDependency.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PluginDependency.

        The id of the plugin that the original plugin depends on  # noqa: E501

        :param id: The id of this PluginDependency.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def load_order(self):
        """Gets the load_order of this PluginDependency.  # noqa: E501

        The load order of the original plugin in relation to the dependency  # noqa: E501

        :return: The load_order of this PluginDependency.  # noqa: E501
        :rtype: str
        """
        return self._load_order

    @load_order.setter
    def load_order(self, load_order):
        """Sets the load_order of this PluginDependency.

        The load order of the original plugin in relation to the dependency  # noqa: E501

        :param load_order: The load_order of this PluginDependency.  # noqa: E501
        :type: str
        """
        if load_order is None:
            raise ValueError("Invalid value for `load_order`, must not be `None`")  # noqa: E501
        allowed_values = ["NONE", "BEFORE", "AFTER"]  # noqa: E501
        if load_order not in allowed_values:
            raise ValueError(
                "Invalid value for `load_order` ({0}), must be one of {1}"  # noqa: E501
                .format(load_order, allowed_values)
            )

        self._load_order = load_order

    @property
    def optional(self):
        """Gets the optional of this PluginDependency.  # noqa: E501

        True if this is an optional dependency, false otherwise  # noqa: E501

        :return: The optional of this PluginDependency.  # noqa: E501
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """Sets the optional of this PluginDependency.

        True if this is an optional dependency, false otherwise  # noqa: E501

        :param optional: The optional of this PluginDependency.  # noqa: E501
        :type: bool
        """
        if optional is None:
            raise ValueError("Invalid value for `optional`, must not be `None`")  # noqa: E501

        self._optional = optional

    @property
    def version(self):
        """Gets the version of this PluginDependency.  # noqa: E501

        The version of the plugin that the original plugin depends on  # noqa: E501

        :return: The version of this PluginDependency.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PluginDependency.

        The version of the plugin that the original plugin depends on  # noqa: E501

        :param version: The version of this PluginDependency.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if issubclass(PluginDependency, dict):
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
        if not isinstance(other, PluginDependency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
