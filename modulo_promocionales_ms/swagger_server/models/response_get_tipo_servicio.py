# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.response_get_tipo_servicio_tiposervicio import ResponseGetTipoServicioTIPOSERVICIO  # noqa: F401,E501
from swagger_server import util


class ResponseGetTipoServicio(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, error_code: int=None, tipo_servicio: List[ResponseGetTipoServicioTIPOSERVICIO]=None, internal_transaction_id: int=None, external_transaction_id: int=None, message: str=None):  # noqa: E501
        """ResponseGetTipoServicio - a model defined in Swagger

        :param error_code: The error_code of this ResponseGetTipoServicio.  # noqa: E501
        :type error_code: int
        :param tipo_servicio: The tipo_servicio of this ResponseGetTipoServicio.  # noqa: E501
        :type tipo_servicio: List[ResponseGetTipoServicioTIPOSERVICIO]
        :param internal_transaction_id: The internal_transaction_id of this ResponseGetTipoServicio.  # noqa: E501
        :type internal_transaction_id: int
        :param external_transaction_id: The external_transaction_id of this ResponseGetTipoServicio.  # noqa: E501
        :type external_transaction_id: int
        :param message: The message of this ResponseGetTipoServicio.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'error_code': int,
            'tipo_servicio': List[ResponseGetTipoServicioTIPOSERVICIO],
            'internal_transaction_id': int,
            'external_transaction_id': int,
            'message': str
        }

        self.attribute_map = {
            'error_code': 'errorCode',
            'tipo_servicio': 'TIPO_SERVICIO',
            'internal_transaction_id': 'internalTransactionId',
            'external_transaction_id': 'externalTransactionId',
            'message': 'message'
        }
        self._error_code = error_code
        self._tipo_servicio = tipo_servicio
        self._internal_transaction_id = internal_transaction_id
        self._external_transaction_id = external_transaction_id
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseGetTipoServicio':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseGetTipo_Servicio of this ResponseGetTipoServicio.  # noqa: E501
        :rtype: ResponseGetTipoServicio
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error_code(self) -> int:
        """Gets the error_code of this ResponseGetTipoServicio.


        :return: The error_code of this ResponseGetTipoServicio.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code: int):
        """Sets the error_code of this ResponseGetTipoServicio.


        :param error_code: The error_code of this ResponseGetTipoServicio.
        :type error_code: int
        """

        self._error_code = error_code

    @property
    def tipo_servicio(self) -> List[ResponseGetTipoServicioTIPOSERVICIO]:
        """Gets the tipo_servicio of this ResponseGetTipoServicio.


        :return: The tipo_servicio of this ResponseGetTipoServicio.
        :rtype: List[ResponseGetTipoServicioTIPOSERVICIO]
        """
        return self._tipo_servicio

    @tipo_servicio.setter
    def tipo_servicio(self, tipo_servicio: List[ResponseGetTipoServicioTIPOSERVICIO]):
        """Sets the tipo_servicio of this ResponseGetTipoServicio.


        :param tipo_servicio: The tipo_servicio of this ResponseGetTipoServicio.
        :type tipo_servicio: List[ResponseGetTipoServicioTIPOSERVICIO]
        """

        self._tipo_servicio = tipo_servicio

    @property
    def internal_transaction_id(self) -> int:
        """Gets the internal_transaction_id of this ResponseGetTipoServicio.


        :return: The internal_transaction_id of this ResponseGetTipoServicio.
        :rtype: int
        """
        return self._internal_transaction_id

    @internal_transaction_id.setter
    def internal_transaction_id(self, internal_transaction_id: int):
        """Sets the internal_transaction_id of this ResponseGetTipoServicio.


        :param internal_transaction_id: The internal_transaction_id of this ResponseGetTipoServicio.
        :type internal_transaction_id: int
        """

        self._internal_transaction_id = internal_transaction_id

    @property
    def external_transaction_id(self) -> int:
        """Gets the external_transaction_id of this ResponseGetTipoServicio.


        :return: The external_transaction_id of this ResponseGetTipoServicio.
        :rtype: int
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: int):
        """Sets the external_transaction_id of this ResponseGetTipoServicio.


        :param external_transaction_id: The external_transaction_id of this ResponseGetTipoServicio.
        :type external_transaction_id: int
        """

        self._external_transaction_id = external_transaction_id

    @property
    def message(self) -> str:
        """Gets the message of this ResponseGetTipoServicio.


        :return: The message of this ResponseGetTipoServicio.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ResponseGetTipoServicio.


        :param message: The message of this ResponseGetTipoServicio.
        :type message: str
        """

        self._message = message
