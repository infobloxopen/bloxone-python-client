# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dns_config.models.forwarder import Forwarder
from typing import Optional, Set
from typing_extensions import Self


class ForwardZoneConfig(BaseModel):
    """
    ForwardZoneConfig
    """

  # noqa: E501
    external_forwarders: Optional[List[Forwarder]] = Field(
        default=None,
        description=
        "Optional. External DNS servers to forward to. Order is not significant."
    )
    hosts: Optional[List[StrictStr]] = Field(
        default=None, description="The resource identifier.")
    internal_forwarders: Optional[List[StrictStr]] = Field(
        default=None, description="The resource identifier.")
    nsgs: Optional[List[StrictStr]] = Field(
        default=None, description="The resource identifier.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "external_forwarders", "hosts", "internal_forwarders", "nsgs"
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ForwardZoneConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in external_forwarders (list)
        _items = []
        if self.external_forwarders:
            for _item in self.external_forwarders:
                if _item:
                    _items.append(_item.to_dict())
            _dict['external_forwarders'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ForwardZoneConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "external_forwarders": [
                Forwarder.from_dict(_item)
                for _item in obj["external_forwarders"]
            ] if obj.get("external_forwarders") is not None else None,
            "hosts":
            obj.get("hosts"),
            "internal_forwarders":
            obj.get("internal_forwarders"),
            "nsgs":
            obj.get("nsgs")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
