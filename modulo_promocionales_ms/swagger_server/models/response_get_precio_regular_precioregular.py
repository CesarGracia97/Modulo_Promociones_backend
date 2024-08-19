# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResponseGetPrecioRegularPRECIOREGULAR(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, precio: float=None):  # noqa: E501
        """ResponseGetPrecioRegularPRECIOREGULAR - a model defined in Swagger

        :param precio: The precio of this ResponseGetPrecioRegularPRECIOREGULAR.  # noqa: E501
        :type precio: float
        """
        self.swagger_types = {
            'precio': float
        }

        self.attribute_map = {
            'precio': 'PRECIO'
        }
        self._precio = precio

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseGetPrecioRegularPRECIOREGULAR':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseGetPrecio_Regular_PRECIO_REGULAR of this ResponseGetPrecioRegularPRECIOREGULAR.  # noqa: E501
        :rtype: ResponseGetPrecioRegularPRECIOREGULAR
        """
        return util.deserialize_model(dikt, cls)

    @property
    def precio(self) -> float:
        """Gets the precio of this ResponseGetPrecioRegularPRECIOREGULAR.


        :return: The precio of this ResponseGetPrecioRegularPRECIOREGULAR.
        :rtype: float
        """
        return self._precio

    @precio.setter
    def precio(self, precio: float):
        """Sets the precio of this ResponseGetPrecioRegularPRECIOREGULAR.


        :param precio: The precio of this ResponseGetPrecioRegularPRECIOREGULAR.
        :type precio: float
        """

        self._precio = precio
