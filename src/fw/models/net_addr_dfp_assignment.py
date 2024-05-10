# coding: utf-8

"""
    BloxOne FW API

    BloxOne Threat Defense Cloud is an extension of the BloxOne Suite that provides visibility into infected and compromised off-premises devices, roaming users, remote sites, and branch offices. You can subscribe to BloxOne Cloud and use its functionality to mitigate and control malware as well as provide unprecedented insight into your network security posture and enable timely action. BloxOne Cloud also offers unified policy management, reporting, and threat analytics across the entire spectrum. Using automated and high-quality threat intelligence feeds and unique behavioral analytics, it automatically stops device communications with C&Cs/botnets and prevents DNS based data exfiltration.  The mission-critical DNS infrastructure can become a vulnerable component in your network when it is inadequately protected by traditional security solutions and consequently used as an attack surface. Compromised DNS services can result in catastrophic network and system failures. To fully protect your network in today’s cyber security threat environment, Infoblox sets a new DNS security standard by offering scalable, enterprise-grade, and integrated protection for your DNS infrastructure.  Through the Infoblox Cloud Services Portal, you can view the status of your subscription and threat intelligence feeds, manage your network scope and roaming end users, and learn more about threats on your networks through the Infoblox Threat Lookup tool and predefined reports. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fw.models.net_addr_dfp_assignment_scope_type import NetAddrDfpAssignmentScopeType
from typing import Optional, Set
from typing_extensions import Self


class NetAddrDfpAssignment(BaseModel):
    """
    Scoped DFP assignment to a policy, scoped via network address (CIDR)
    """ # noqa: E501
    addr_net: Optional[StrictStr] = Field(
        default=None,
        description=
        "network address in IPv4 CIDR (address/bitmask length) string format")
    dfp_ids: Optional[List[StrictInt]] = Field(
        default=None,
        description=
        "The list of identifiers of DFPs that have association with this scope."
    )
    dfp_service_ids: Optional[List[StrictStr]] = None
    end: Optional[StrictStr] = None
    external_scope_id: Optional[StrictStr] = Field(
        default=None, description="external scope ID, UUID")
    host_id: Optional[StrictStr] = Field(default=None,
                                         description="Host reference, UUID")
    ip_space_id: Optional[StrictStr] = Field(
        default=None, description="IPSpace reference, UUID")
    scope_type: Optional[NetAddrDfpAssignmentScopeType] = None
    start: Optional[StrictStr] = Field(
        default=None,
        description="Start and end pair of addresses used for range scope type"
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "addr_net", "dfp_ids", "dfp_service_ids", "end", "external_scope_id",
        "host_id", "ip_space_id", "scope_type", "start"
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
        """Create an instance of NetAddrDfpAssignment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "dfp_ids",
            "dfp_service_ids",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NetAddrDfpAssignment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addr_net":
            obj.get("addr_net"),
            "dfp_ids":
            obj.get("dfp_ids"),
            "dfp_service_ids":
            obj.get("dfp_service_ids"),
            "end":
            obj.get("end"),
            "external_scope_id":
            obj.get("external_scope_id"),
            "host_id":
            obj.get("host_id"),
            "ip_space_id":
            obj.get("ip_space_id"),
            "scope_type":
            obj.get("scope_type"),
            "start":
            obj.get("start")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
