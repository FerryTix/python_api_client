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

class WaitingPassenger(object):
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
        'ticket_class': 'TicketClass',
        'waiting_since': 'datetime'
    }

    attribute_map = {
        'ticket_class': 'ticketClass',
        'waiting_since': 'waitingSince'
    }

    def __init__(self, ticket_class=None, waiting_since=None):  # noqa: E501
        """WaitingPassenger - a model defined in Swagger"""  # noqa: E501
        self._ticket_class = None
        self._waiting_since = None
        self.discriminator = None
        if ticket_class is not None:
            self.ticket_class = ticket_class
        if waiting_since is not None:
            self.waiting_since = waiting_since

    @property
    def ticket_class(self):
        """Gets the ticket_class of this WaitingPassenger.  # noqa: E501


        :return: The ticket_class of this WaitingPassenger.  # noqa: E501
        :rtype: TicketClass
        """
        return self._ticket_class

    @ticket_class.setter
    def ticket_class(self, ticket_class):
        """Sets the ticket_class of this WaitingPassenger.


        :param ticket_class: The ticket_class of this WaitingPassenger.  # noqa: E501
        :type: TicketClass
        """

        self._ticket_class = ticket_class

    @property
    def waiting_since(self):
        """Gets the waiting_since of this WaitingPassenger.  # noqa: E501


        :return: The waiting_since of this WaitingPassenger.  # noqa: E501
        :rtype: datetime
        """
        return self._waiting_since

    @waiting_since.setter
    def waiting_since(self, waiting_since):
        """Sets the waiting_since of this WaitingPassenger.


        :param waiting_since: The waiting_since of this WaitingPassenger.  # noqa: E501
        :type: datetime
        """

        self._waiting_since = waiting_since

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
        if issubclass(WaitingPassenger, dict):
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
        if not isinstance(other, WaitingPassenger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
