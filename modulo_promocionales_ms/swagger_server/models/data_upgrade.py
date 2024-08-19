# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DataUpgrade(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, upgrade: int=None, mes_inicio_upgrade: int=None, mes_fin_upgrade: str=None):  # noqa: E501
        """DataUpgrade - a model defined in Swagger

        :param upgrade: The upgrade of this DataUpgrade.  # noqa: E501
        :type upgrade: int
        :param mes_inicio_upgrade: The mes_inicio_upgrade of this DataUpgrade.  # noqa: E501
        :type mes_inicio_upgrade: int
        :param mes_fin_upgrade: The mes_fin_upgrade of this DataUpgrade.  # noqa: E501
        :type mes_fin_upgrade: str
        """
        self.swagger_types = {
            'upgrade': int,
            'mes_inicio_upgrade': int,
            'mes_fin_upgrade': str
        }

        self.attribute_map = {
            'upgrade': 'UPGRADE',
            'mes_inicio_upgrade': 'Mes Inicio UPGRADE',
            'mes_fin_upgrade': 'Mes Fin UPGRADE'
        }
        self._upgrade = upgrade
        self._mes_inicio_upgrade = mes_inicio_upgrade
        self._mes_fin_upgrade = mes_fin_upgrade

    @classmethod
    def from_dict(cls, dikt) -> 'DataUpgrade':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DataUpgrade of this DataUpgrade.  # noqa: E501
        :rtype: DataUpgrade
        """
        return util.deserialize_model(dikt, cls)

    @property
    def upgrade(self) -> int:
        """Gets the upgrade of this DataUpgrade.


        :return: The upgrade of this DataUpgrade.
        :rtype: int
        """
        return self._upgrade

    @upgrade.setter
    def upgrade(self, upgrade: int):
        """Sets the upgrade of this DataUpgrade.


        :param upgrade: The upgrade of this DataUpgrade.
        :type upgrade: int
        """
        if upgrade is None:
            raise ValueError("Invalid value for `upgrade`, must not be `None`")  # noqa: E501

        self._upgrade = upgrade

    @property
    def mes_inicio_upgrade(self) -> int:
        """Gets the mes_inicio_upgrade of this DataUpgrade.


        :return: The mes_inicio_upgrade of this DataUpgrade.
        :rtype: int
        """
        return self._mes_inicio_upgrade

    @mes_inicio_upgrade.setter
    def mes_inicio_upgrade(self, mes_inicio_upgrade: int):
        """Sets the mes_inicio_upgrade of this DataUpgrade.


        :param mes_inicio_upgrade: The mes_inicio_upgrade of this DataUpgrade.
        :type mes_inicio_upgrade: int
        """
        if mes_inicio_upgrade is None:
            raise ValueError("Invalid value for `mes_inicio_upgrade`, must not be `None`")  # noqa: E501

        self._mes_inicio_upgrade = mes_inicio_upgrade

    @property
    def mes_fin_upgrade(self) -> str:
        """Gets the mes_fin_upgrade of this DataUpgrade.


        :return: The mes_fin_upgrade of this DataUpgrade.
        :rtype: str
        """
        return self._mes_fin_upgrade

    @mes_fin_upgrade.setter
    def mes_fin_upgrade(self, mes_fin_upgrade: str):
        """Sets the mes_fin_upgrade of this DataUpgrade.


        :param mes_fin_upgrade: The mes_fin_upgrade of this DataUpgrade.
        :type mes_fin_upgrade: str
        """
        if mes_fin_upgrade is None:
            raise ValueError("Invalid value for `mes_fin_upgrade`, must not be `None`")  # noqa: E501

        self._mes_fin_upgrade = mes_fin_upgrade
