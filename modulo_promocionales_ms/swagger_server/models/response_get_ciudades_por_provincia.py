# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.response_get_ciudades_cities import ResponseGetCiudadesCITIES  # noqa: F401,E501
from swagger_server import util


class ResponseGetCiudadesPorProvincia(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, error_code: int=None, citiesx_prov: List[ResponseGetCiudadesCITIES]=None, internal_transaction_id: int=None, external_transaction_id: int=None, message: str=None):  # noqa: E501
        """ResponseGetCiudadesPorProvincia - a model defined in Swagger

        :param error_code: The error_code of this ResponseGetCiudadesPorProvincia.  # noqa: E501
        :type error_code: int
        :param citiesx_prov: The citiesx_prov of this ResponseGetCiudadesPorProvincia.  # noqa: E501
        :type citiesx_prov: List[ResponseGetCiudadesCITIES]
        :param internal_transaction_id: The internal_transaction_id of this ResponseGetCiudadesPorProvincia.  # noqa: E501
        :type internal_transaction_id: int
        :param external_transaction_id: The external_transaction_id of this ResponseGetCiudadesPorProvincia.  # noqa: E501
        :type external_transaction_id: int
        :param message: The message of this ResponseGetCiudadesPorProvincia.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'error_code': int,
            'citiesx_prov': List[ResponseGetCiudadesCITIES],
            'internal_transaction_id': int,
            'external_transaction_id': int,
            'message': str
        }

        self.attribute_map = {
            'error_code': 'errorCode',
            'citiesx_prov': 'CITIESxPROV',
            'internal_transaction_id': 'internalTransactionId',
            'external_transaction_id': 'externalTransactionId',
            'message': 'message'
        }
        self._error_code = error_code
        self._citiesx_prov = citiesx_prov
        self._internal_transaction_id = internal_transaction_id
        self._external_transaction_id = external_transaction_id
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseGetCiudadesPorProvincia':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseGetCiudadesPorProvincia of this ResponseGetCiudadesPorProvincia.  # noqa: E501
        :rtype: ResponseGetCiudadesPorProvincia
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error_code(self) -> int:
        """Gets the error_code of this ResponseGetCiudadesPorProvincia.


        :return: The error_code of this ResponseGetCiudadesPorProvincia.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code: int):
        """Sets the error_code of this ResponseGetCiudadesPorProvincia.


        :param error_code: The error_code of this ResponseGetCiudadesPorProvincia.
        :type error_code: int
        """

        self._error_code = error_code

    @property
    def citiesx_prov(self) -> List[ResponseGetCiudadesCITIES]:
        """Gets the citiesx_prov of this ResponseGetCiudadesPorProvincia.


        :return: The citiesx_prov of this ResponseGetCiudadesPorProvincia.
        :rtype: List[ResponseGetCiudadesCITIES]
        """
        return self._citiesx_prov

    @citiesx_prov.setter
    def citiesx_prov(self, citiesx_prov: List[ResponseGetCiudadesCITIES]):
        """Sets the citiesx_prov of this ResponseGetCiudadesPorProvincia.


        :param citiesx_prov: The citiesx_prov of this ResponseGetCiudadesPorProvincia.
        :type citiesx_prov: List[ResponseGetCiudadesCITIES]
        """

        self._citiesx_prov = citiesx_prov

    @property
    def internal_transaction_id(self) -> int:
        """Gets the internal_transaction_id of this ResponseGetCiudadesPorProvincia.


        :return: The internal_transaction_id of this ResponseGetCiudadesPorProvincia.
        :rtype: int
        """
        return self._internal_transaction_id

    @internal_transaction_id.setter
    def internal_transaction_id(self, internal_transaction_id: int):
        """Sets the internal_transaction_id of this ResponseGetCiudadesPorProvincia.


        :param internal_transaction_id: The internal_transaction_id of this ResponseGetCiudadesPorProvincia.
        :type internal_transaction_id: int
        """

        self._internal_transaction_id = internal_transaction_id

    @property
    def external_transaction_id(self) -> int:
        """Gets the external_transaction_id of this ResponseGetCiudadesPorProvincia.


        :return: The external_transaction_id of this ResponseGetCiudadesPorProvincia.
        :rtype: int
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: int):
        """Sets the external_transaction_id of this ResponseGetCiudadesPorProvincia.


        :param external_transaction_id: The external_transaction_id of this ResponseGetCiudadesPorProvincia.
        :type external_transaction_id: int
        """

        self._external_transaction_id = external_transaction_id

    @property
    def message(self) -> str:
        """Gets the message of this ResponseGetCiudadesPorProvincia.


        :return: The message of this ResponseGetCiudadesPorProvincia.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ResponseGetCiudadesPorProvincia.


        :param message: The message of this ResponseGetCiudadesPorProvincia.
        :type message: str
        """

        self._message = message
