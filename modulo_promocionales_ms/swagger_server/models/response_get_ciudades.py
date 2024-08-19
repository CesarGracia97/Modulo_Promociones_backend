# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.response_get_ciudades_cities import ResponseGetCiudadesCITIES  # noqa: F401,E501
from swagger_server import util


class ResponseGetCiudades(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, error_code: int=None, cities: List[ResponseGetCiudadesCITIES]=None, internal_transaction_id: int=None, external_transaction_id: int=None, message: str=None):  # noqa: E501
        """ResponseGetCiudades - a model defined in Swagger

        :param error_code: The error_code of this ResponseGetCiudades.  # noqa: E501
        :type error_code: int
        :param cities: The cities of this ResponseGetCiudades.  # noqa: E501
        :type cities: List[ResponseGetCiudadesCITIES]
        :param internal_transaction_id: The internal_transaction_id of this ResponseGetCiudades.  # noqa: E501
        :type internal_transaction_id: int
        :param external_transaction_id: The external_transaction_id of this ResponseGetCiudades.  # noqa: E501
        :type external_transaction_id: int
        :param message: The message of this ResponseGetCiudades.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'error_code': int,
            'cities': List[ResponseGetCiudadesCITIES],
            'internal_transaction_id': int,
            'external_transaction_id': int,
            'message': str
        }

        self.attribute_map = {
            'error_code': 'errorCode',
            'cities': 'CITIES',
            'internal_transaction_id': 'internalTransactionId',
            'external_transaction_id': 'externalTransactionId',
            'message': 'message'
        }
        self._error_code = error_code
        self._cities = cities
        self._internal_transaction_id = internal_transaction_id
        self._external_transaction_id = external_transaction_id
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseGetCiudades':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseGetCiudades of this ResponseGetCiudades.  # noqa: E501
        :rtype: ResponseGetCiudades
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error_code(self) -> int:
        """Gets the error_code of this ResponseGetCiudades.


        :return: The error_code of this ResponseGetCiudades.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code: int):
        """Sets the error_code of this ResponseGetCiudades.


        :param error_code: The error_code of this ResponseGetCiudades.
        :type error_code: int
        """

        self._error_code = error_code

    @property
    def cities(self) -> List[ResponseGetCiudadesCITIES]:
        """Gets the cities of this ResponseGetCiudades.


        :return: The cities of this ResponseGetCiudades.
        :rtype: List[ResponseGetCiudadesCITIES]
        """
        return self._cities

    @cities.setter
    def cities(self, cities: List[ResponseGetCiudadesCITIES]):
        """Sets the cities of this ResponseGetCiudades.


        :param cities: The cities of this ResponseGetCiudades.
        :type cities: List[ResponseGetCiudadesCITIES]
        """

        self._cities = cities

    @property
    def internal_transaction_id(self) -> int:
        """Gets the internal_transaction_id of this ResponseGetCiudades.


        :return: The internal_transaction_id of this ResponseGetCiudades.
        :rtype: int
        """
        return self._internal_transaction_id

    @internal_transaction_id.setter
    def internal_transaction_id(self, internal_transaction_id: int):
        """Sets the internal_transaction_id of this ResponseGetCiudades.


        :param internal_transaction_id: The internal_transaction_id of this ResponseGetCiudades.
        :type internal_transaction_id: int
        """

        self._internal_transaction_id = internal_transaction_id

    @property
    def external_transaction_id(self) -> int:
        """Gets the external_transaction_id of this ResponseGetCiudades.


        :return: The external_transaction_id of this ResponseGetCiudades.
        :rtype: int
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: int):
        """Sets the external_transaction_id of this ResponseGetCiudades.


        :param external_transaction_id: The external_transaction_id of this ResponseGetCiudades.
        :type external_transaction_id: int
        """

        self._external_transaction_id = external_transaction_id

    @property
    def message(self) -> str:
        """Gets the message of this ResponseGetCiudades.


        :return: The message of this ResponseGetCiudades.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ResponseGetCiudades.


        :param message: The message of this ResponseGetCiudades.
        :type message: str
        """

        self._message = message
