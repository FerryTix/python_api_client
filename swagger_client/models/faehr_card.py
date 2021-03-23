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

class FaehrCard(object):
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
        'owned_by': 'str',
        'balance': 'int',
        'issued_at': 'datetime',
        'issued_by': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'owned_by': 'ownedBy',
        'balance': 'balance',
        'issued_at': 'issuedAt',
        'issued_by': 'issuedBy'
    }

    def __init__(self, uuid=None, owned_by=None, balance=None, issued_at=None, issued_by=None):  # noqa: E501
        """FaehrCard - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._owned_by = None
        self._balance = None
        self._issued_at = None
        self._issued_by = None
        self.discriminator = None
        if uuid is not None:
            self.uuid = uuid
        if owned_by is not None:
            self.owned_by = owned_by
        if balance is not None:
            self.balance = balance
        if issued_at is not None:
            self.issued_at = issued_at
        if issued_by is not None:
            self.issued_by = issued_by

    @property
    def uuid(self):
        """Gets the uuid of this FaehrCard.  # noqa: E501


        :return: The uuid of this FaehrCard.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this FaehrCard.


        :param uuid: The uuid of this FaehrCard.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def owned_by(self):
        """Gets the owned_by of this FaehrCard.  # noqa: E501


        :return: The owned_by of this FaehrCard.  # noqa: E501
        :rtype: str
        """
        return self._owned_by

    @owned_by.setter
    def owned_by(self, owned_by):
        """Sets the owned_by of this FaehrCard.


        :param owned_by: The owned_by of this FaehrCard.  # noqa: E501
        :type: str
        """

        self._owned_by = owned_by

    @property
    def balance(self):
        """Gets the balance of this FaehrCard.  # noqa: E501


        :return: The balance of this FaehrCard.  # noqa: E501
        :rtype: int
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this FaehrCard.


        :param balance: The balance of this FaehrCard.  # noqa: E501
        :type: int
        """

        self._balance = balance

    @property
    def issued_at(self):
        """Gets the issued_at of this FaehrCard.  # noqa: E501


        :return: The issued_at of this FaehrCard.  # noqa: E501
        :rtype: datetime
        """
        return self._issued_at

    @issued_at.setter
    def issued_at(self, issued_at):
        """Sets the issued_at of this FaehrCard.


        :param issued_at: The issued_at of this FaehrCard.  # noqa: E501
        :type: datetime
        """

        self._issued_at = issued_at

    @property
    def issued_by(self):
        """Gets the issued_by of this FaehrCard.  # noqa: E501


        :return: The issued_by of this FaehrCard.  # noqa: E501
        :rtype: str
        """
        return self._issued_by

    @issued_by.setter
    def issued_by(self, issued_by):
        """Sets the issued_by of this FaehrCard.


        :param issued_by: The issued_by of this FaehrCard.  # noqa: E501
        :type: str
        """

        self._issued_by = issued_by

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
        if issubclass(FaehrCard, dict):
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
        if not isinstance(other, FaehrCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other