# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a Universal DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ipam.models.access_filter import AccessFilter
from ipam.models.dhcp_options_inheritance import DHCPOptionsInheritance
from ipam.models.exclusion_range import ExclusionRange
from ipam.models.inheritance_assigned_host import InheritanceAssignedHost
from ipam.models.option_item import OptionItem
from ipam.models.utilization import Utilization
from ipam.models.utilization_threshold import UtilizationThreshold
from ipam.models.utilization_v6 import UtilizationV6
from typing import Optional, Set
from typing_extensions import Self


class Range(BaseModel):
    """
    A __Range__ object (_ipam/range_) represents a set of contiguous IP addresses in the same IP space with no gap, expressed as a (start, end) pair within a given subnet that are grouped together for administrative purpose and protocol management. The start and end values are not required to align with CIDR boundaries. 
    """ # noqa: E501
    comment: Optional[StrictStr] = Field(
        default=None,
        description=
        "The description for the range. May contain 0 to 1024 characters. Can include UTF-8."
    )
    compartment_id: Optional[StrictStr] = Field(
        default=None,
        description=
        "The compartment associated with the object. If no compartment is associated with the object, the value defaults to empty."
    )
    created_at: Optional[datetime] = Field(
        default=None, description="Time when the object has been created.")
    dhcp_host: Optional[StrictStr] = Field(
        default=None, description="The resource identifier.")
    dhcp_options: Optional[List[OptionItem]] = Field(
        default=None,
        description=
        "The list of DHCP options. May be either a specific option or a group of options."
    )
    disable_dhcp: Optional[StrictBool] = Field(
        default=None,
        description=
        "Optional. _true_ to disable object. A disabled object is effectively non-existent when generating configuration.  Defaults to _false_."
    )
    end: StrictStr = Field(description="The end IP address of the range.")
    exclusion_ranges: Optional[List[ExclusionRange]] = Field(
        default=None,
        description=
        "The list of all exclusion ranges in the scope of the range.")
    filters: Optional[List[AccessFilter]] = Field(
        default=None,
        description="The list of all allow/deny filters of the range.")
    id: Optional[StrictStr] = Field(default=None,
                                    description="The resource identifier.")
    inheritance_assigned_hosts: Optional[List[InheritanceAssignedHost]] = Field(
        default=None,
        description="The list of the inheritance assigned hosts of the object."
    )
    inheritance_parent: Optional[StrictStr] = Field(
        default=None, description="The resource identifier.")
    inheritance_sources: Optional[DHCPOptionsInheritance] = Field(
        default=None,
        description="The DHCP inheritance configuration for the range.")
    name: Optional[StrictStr] = Field(
        default=None,
        description=
        "The name of the range. May contain 1 to 256 characters. Can include UTF-8."
    )
    parent: Optional[StrictStr] = Field(default=None,
                                        description="The resource identifier.")
    protocol: Optional[StrictStr] = Field(
        default=None, description="The type of protocol (_ip4_ or _ip6_).")
    space: Optional[StrictStr] = Field(default=None,
                                       description="The resource identifier.")
    space_name: Optional[StrictStr] = Field(
        default=None,
        description="The name of the IP Space the range belongs to.")
    start: StrictStr = Field(description="The start IP address of the range.")
    tags: Optional[Dict[str, Any]] = Field(
        default=None, description="The tags for the range in JSON format.")
    threshold: Optional[UtilizationThreshold] = Field(
        default=None,
        description="The utilization threshold settings for the range.")
    updated_at: Optional[datetime] = Field(
        default=None,
        description=
        "Time when the object has been updated. Equals to _created_at_ if not updated after creation."
    )
    utilization: Optional[Utilization] = Field(
        default=None,
        description=
        "The utilization statistics of IPV4 addresses for the range.")
    utilization_v6: Optional[UtilizationV6] = Field(
        default=None,
        description="The utilization of IPV6 addresses in the range.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "comment", "compartment_id", "created_at", "dhcp_host", "dhcp_options",
        "disable_dhcp", "end", "exclusion_ranges", "filters", "id",
        "inheritance_assigned_hosts", "inheritance_parent",
        "inheritance_sources", "name", "parent", "protocol", "space",
        "space_name", "start", "tags", "threshold", "updated_at",
        "utilization", "utilization_v6"
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
        """Create an instance of Range from a JSON string"""
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
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "compartment_id",
            "created_at",
            "id",
            "inheritance_assigned_hosts",
            "protocol",
            "space_name",
            "updated_at",
            "utilization",
            "utilization_v6",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in dhcp_options (list)
        _items = []
        if self.dhcp_options:
            for _item in self.dhcp_options:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dhcp_options'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in exclusion_ranges (list)
        _items = []
        if self.exclusion_ranges:
            for _item in self.exclusion_ranges:
                if _item:
                    _items.append(_item.to_dict())
            _dict['exclusion_ranges'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item in self.filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['filters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in inheritance_assigned_hosts (list)
        _items = []
        if self.inheritance_assigned_hosts:
            for _item in self.inheritance_assigned_hosts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['inheritance_assigned_hosts'] = _items
        # override the default output from pydantic by calling `to_dict()` of inheritance_sources
        if self.inheritance_sources:
            _dict['inheritance_sources'] = self.inheritance_sources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of threshold
        if self.threshold:
            _dict['threshold'] = self.threshold.to_dict()
        # override the default output from pydantic by calling `to_dict()` of utilization
        if self.utilization:
            _dict['utilization'] = self.utilization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of utilization_v6
        if self.utilization_v6:
            _dict['utilization_v6'] = self.utilization_v6.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Range from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "comment":
            obj.get("comment"),
            "compartment_id":
            obj.get("compartment_id"),
            "created_at":
            obj.get("created_at"),
            "dhcp_host":
            obj.get("dhcp_host"),
            "dhcp_options":
            [OptionItem.from_dict(_item) for _item in obj["dhcp_options"]]
            if obj.get("dhcp_options") is not None else None,
            "disable_dhcp":
            obj.get("disable_dhcp"),
            "end":
            obj.get("end"),
            "exclusion_ranges": [
                ExclusionRange.from_dict(_item)
                for _item in obj["exclusion_ranges"]
            ] if obj.get("exclusion_ranges") is not None else None,
            "filters":
            [AccessFilter.from_dict(_item) for _item in obj["filters"]]
            if obj.get("filters") is not None else None,
            "id":
            obj.get("id"),
            "inheritance_assigned_hosts": [
                InheritanceAssignedHost.from_dict(_item)
                for _item in obj["inheritance_assigned_hosts"]
            ] if obj.get("inheritance_assigned_hosts") is not None else None,
            "inheritance_parent":
            obj.get("inheritance_parent"),
            "inheritance_sources":
            DHCPOptionsInheritance.from_dict(obj["inheritance_sources"])
            if obj.get("inheritance_sources") is not None else None,
            "name":
            obj.get("name"),
            "parent":
            obj.get("parent"),
            "protocol":
            obj.get("protocol"),
            "space":
            obj.get("space"),
            "space_name":
            obj.get("space_name"),
            "start":
            obj.get("start"),
            "tags":
            obj.get("tags"),
            "threshold":
            UtilizationThreshold.from_dict(obj["threshold"])
            if obj.get("threshold") is not None else None,
            "updated_at":
            obj.get("updated_at"),
            "utilization":
            Utilization.from_dict(obj["utilization"])
            if obj.get("utilization") is not None else None,
            "utilization_v6":
            UtilizationV6.from_dict(obj["utilization_v6"])
            if obj.get("utilization_v6") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
