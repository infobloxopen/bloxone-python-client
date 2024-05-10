# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class DHCPInfo(BaseModel):
    """
    The __DHCPInfo__ object represents the DHCP information associated with an address object.
    """ # noqa: E501
    client_hostname: Optional[StrictStr] = Field(
        default=None,
        description="The DHCP host name associated with this client.")
    client_hwaddr: Optional[StrictStr] = Field(
        default=None,
        description="The hardware address associated with this client.")
    client_id: Optional[StrictStr] = Field(
        default=None, description="The ID associated with this client.")
    end: Optional[datetime] = Field(
        default=None,
        description=
        "The timestamp at which the _state_, when set to _leased_, will be changed to _free_."
    )
    fingerprint: Optional[StrictStr] = Field(
        default=None,
        description="The DHCP fingerprint for the associated lease.")
    iaid: Optional[StrictInt] = Field(
        default=None,
        description=
        "Identity Association Identifier (IAID) of the lease. Applicable only for DHCPv6."
    )
    lease_type: Optional[StrictStr] = Field(
        default=None,
        description=
        "Lease type. Applicable only for address under DHCP control. The value can be empty for address not under DHCP control.  Valid values are: * _DHCPv6NonTemporaryAddress_: DHCPv6 non-temporary address (NA) * _DHCPv6TemporaryAddress_: DHCPv6 temporary address (TA) * _DHCPv6PrefixDelegation_: DHCPv6 prefix delegation (PD) * _DHCPv4_: DHCPv4 lease"
    )
    preferred_lifetime: Optional[datetime] = Field(
        default=None,
        description=
        "The length of time that a valid address is preferred (i.e., the time until deprecation). When the preferred lifetime expires, the address becomes deprecated on the client. It is still considered leased on the server. Applicable only for DHCPv6."
    )
    remain: Optional[StrictInt] = Field(
        default=None,
        description=
        "The remaining time, in seconds, until which the _state_, when set to _leased_, will remain in that state."
    )
    start: Optional[datetime] = Field(
        default=None,
        description="The timestamp at which _state_ was first set to _leased_."
    )
    state: Optional[StrictStr] = Field(
        default=None,
        description=
        "Indicates the status of this IP address from a DHCP protocol standpoint as:   * _none_: Address is not under DHCP control.   * _free_: Address is under DHCP control but has no lease currently assigned.   * _leased_: Address is under DHCP control and has a lease currently assigned. The lease details are contained in the matching _dhcp/lease_ resource."
    )
    state_ts: Optional[datetime] = Field(
        default=None,
        description="The timestamp at which the _state_ was last reported.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "client_hostname", "client_hwaddr", "client_id", "end", "fingerprint",
        "iaid", "lease_type", "preferred_lifetime", "remain", "start", "state",
        "state_ts"
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
        """Create an instance of DHCPInfo from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "client_hostname",
            "client_hwaddr",
            "client_id",
            "end",
            "fingerprint",
            "iaid",
            "lease_type",
            "preferred_lifetime",
            "remain",
            "start",
            "state",
            "state_ts",
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
        """Create an instance of DHCPInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "client_hostname":
            obj.get("client_hostname"),
            "client_hwaddr":
            obj.get("client_hwaddr"),
            "client_id":
            obj.get("client_id"),
            "end":
            obj.get("end"),
            "fingerprint":
            obj.get("fingerprint"),
            "iaid":
            obj.get("iaid"),
            "lease_type":
            obj.get("lease_type"),
            "preferred_lifetime":
            obj.get("preferred_lifetime"),
            "remain":
            obj.get("remain"),
            "start":
            obj.get("start"),
            "state":
            obj.get("state"),
            "state_ts":
            obj.get("state_ts")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
