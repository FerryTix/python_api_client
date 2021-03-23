# coding: utf-8

"""
    FerryTix

    This is the api for the FerryTix Passenger Ferry Ticketing System, that is both accessible to the vending machines and to other clients.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: hendrik.lankers.hl@googlemail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Payment(object):
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
        'uuid': 'str',
        'amount': 'int',
        'method': 'PaymentMethod'
    }

    attribute_map = {
        'uuid': 'uuid',
        'amount': 'amount',
        'method': 'method'
    }

    def __init__(self, uuid=None, amount=None, method=None):  # noqa: E501
        """Payment - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._amount = None
        self._method = None
        self.discriminator = None
        if uuid is not None:
            self.uuid = uuid
        if amount is not None:
            self.amount = amount
        if method is not None:
            self.method = method

    @property
    def uuid(self):
        """Gets the uuid of this Payment.  # noqa: E501


        :return: The uuid of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Payment.


        :param uuid: The uuid of this Payment.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def amount(self):
        """Gets the amount of this Payment.  # noqa: E501


        :return: The amount of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Payment.


        :param amount: The amount of this Payment.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def method(self):
        """Gets the method of this Payment.  # noqa: E501


        :return: The method of this Payment.  # noqa: E501
        :rtype: PaymentMethod
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Payment.


        :param method: The method of this Payment.  # noqa: E501
        :type: PaymentMethod
        """

        self._method = method

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
        if issubclass(Payment, dict):
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
        if not isinstance(other, Payment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
