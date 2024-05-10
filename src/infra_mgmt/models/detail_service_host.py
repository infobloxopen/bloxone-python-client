# coding: utf-8

"""
    Infrastructure Management API

    The **Infrastructure Management API** provides a RESTful interface to manage Infrastructure Hosts and Services objects.  The following is a list of the different Services and their string types (the string types are to be used with the APIs for the `service_type` field):  | Service name | Service type |   | ------ | ------ |   | Access Authentication | authn |   | Anycast | anycast |   | Data Connector | cdc |   | DHCP | dhcp |   | DNS | dns |   | DNS Forwarding Proxy | dfp |   | NIOS Grid Connector | orpheus |   | MS AD Sync | msad |   | NTP | ntp |   | BGP | bgp |   | RIP | rip |   | OSPF | ospf |    ---   ### Hosts API  The Hosts API is used to manage the Infrastructure Host resources. These include various operations related to hosts such as viewing, creating, updating, replacing, disconnecting, and deleting Hosts. Management of Hosts is done from the Cloud Services Portal (CSP) by navigating to the Manage -> Infrastructure -> Hosts tab.  ---   ### Services API  The Services API is used to manage the Infrastructure Service resources (a.k.a. BloxOne applications). These include various operations related to hosts such as viewing, creating, updating, starting/stopping, configuring, and deleting Services. Management of Services is done from the Cloud Services Portal (CSP) by navigating to the Manage -> Infrastructure -> Services tab.  ---   ### Detail APIs  The Detail APIs are read-only APIs used to list all the Infrastructure resources (Hosts and Services). Each resource record returned also contains information about its other associated resources and the status information for itself and the associated resource(s) (i.e., Host/Service status).  ---   

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
from infra_mgmt.models.detail_service_host_config import DetailServiceHostConfig
from typing import Optional, Set
from typing_extensions import Self


class DetailServiceHost(BaseModel):
    """
    DetailServiceHost
    """

  # noqa: E501
    composite_status: Optional[StrictStr] = Field(
        default=None,
        description=
        "Composite Status of the Host (`online`, `degraded`, `error`, `offline`, `pending`, `awaiting approval`)."
    )
    config: Optional[DetailServiceHostConfig] = None
    display_name: Optional[StrictStr] = Field(
        default=None, description="The name of the Host (unique).")
    id: Optional[StrictStr] = Field(default=None,
                                    description="The resource identifier.")
    ip_address: Optional[StrictStr] = Field(
        default=None, description="The IP address of the Host.")
    legacy_id: Optional[StrictStr] = Field(
        default=None, description="The legacy Host object identifier.")
    maintenance_mode: Optional[StrictStr] = None
    ophid: Optional[StrictStr] = Field(
        default=None,
        description=
        "The unique On-Prem Host ID generated by the On-Prem device and assigned to the Host once it is registered and logged into the Infoblox Cloud."
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "composite_status", "config", "display_name", "id", "ip_address",
        "legacy_id", "maintenance_mode", "ophid"
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
        """Create an instance of DetailServiceHost from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "id",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DetailServiceHost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "composite_status":
            obj.get("composite_status"),
            "config":
            DetailServiceHostConfig.from_dict(obj["config"])
            if obj.get("config") is not None else None,
            "display_name":
            obj.get("display_name"),
            "id":
            obj.get("id"),
            "ip_address":
            obj.get("ip_address"),
            "legacy_id":
            obj.get("legacy_id"),
            "maintenance_mode":
            obj.get("maintenance_mode"),
            "ophid":
            obj.get("ophid")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
