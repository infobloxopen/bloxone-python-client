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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dns_config.models.host_associated_server import HostAssociatedServer
from dns_config.models.host_inheritance import HostInheritance
from dns_config.models.kerberos_key import KerberosKey
from typing import Optional, Set
from typing_extensions import Self


class Host(BaseModel):
    """
    A DNS Host (_dns/host_) object associates DNS configuraton with hosts.   Automatically created and destroyed based on the hosts known to the platform.
    """ # noqa: E501
    absolute_name: Optional[StrictStr] = Field(default=None,
                                               description="Host FQDN.")
    address: Optional[StrictStr] = Field(
        default=None, description="Host's primary IP Address.")
    anycast_addresses: Optional[List[StrictStr]] = Field(
        default=None,
        description=
        "Anycast address configured to the host. Order is not significant.")
    associated_server: Optional[HostAssociatedServer] = None
    comment: Optional[StrictStr] = Field(default=None,
                                         description="Host description.")
    current_version: Optional[StrictStr] = Field(
        default=None, description="Host current version.")
    dfp: Optional[StrictBool] = Field(
        default=None,
        description=
        "Below _dfp_ field is deprecated and not supported anymore. The indication whether or not BloxOne DDI DNS and BloxOne TD DFP are both active on the host will be migrated into the new _dfp_service_ field."
    )
    dfp_service: Optional[StrictStr] = Field(
        default=None,
        description=
        "DFP service indicates whether or not BloxOne DDI DNS and BloxOne TD DFP are both active on the host. If so, BloxOne DDI DNS will augment recursive queries and forward them to BloxOne TD DFP. Allowed values:  * _unavailable_: BloxOne TD DFP application is not available,  * _enabled_: BloxOne TD DFP application is available and enabled,  * _disabled_: BloxOne TD DFP application is available but disabled."
    )
    id: Optional[StrictStr] = Field(default=None,
                                    description="The resource identifier.")
    inheritance_sources: Optional[HostInheritance] = None
    kerberos_keys: Optional[List[KerberosKey]] = Field(
        default=None,
        description=
        "Optional. _kerberos_keys_ contains a list of keys for GSS-TSIG signed dynamic updates.  Defaults to empty."
    )
    name: Optional[StrictStr] = Field(default=None,
                                      description="Host display name.")
    ophid: Optional[StrictStr] = Field(default=None,
                                       description="On-Prem Host ID.")
    protocol_absolute_name: Optional[StrictStr] = Field(
        default=None, description="Host FQDN in punycode.")
    provider_id: Optional[StrictStr] = Field(
        default=None, description="External provider identifier.")
    server: Optional[StrictStr] = Field(default=None,
                                        description="The resource identifier.")
    site_id: Optional[StrictStr] = Field(default=None,
                                         description="Host site ID.")
    tags: Optional[Dict[str,
                        Any]] = Field(default=None,
                                      description="Host tagging specifics.")
    type: Optional[StrictStr] = Field(
        default=None,
        description=
        "Defines the type of host. Allowed values:  * _bloxone_ddi_: host type is BloxOne DDI,  * _microsoft_azure_: host type is Microsoft Azure,  * _amazon_web_service_: host type is Amazon Web Services,  * _microsoft_active_directory_: host type is Microsoft Active Directory,  * _google_cloud_platform_: host type is Google Cloud Platform."
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "absolute_name", "address", "anycast_addresses", "associated_server",
        "comment", "current_version", "dfp", "dfp_service", "id",
        "inheritance_sources", "kerberos_keys", "name", "ophid",
        "protocol_absolute_name", "provider_id", "server", "site_id", "tags",
        "type"
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
        """Create an instance of Host from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "absolute_name",
            "address",
            "anycast_addresses",
            "comment",
            "current_version",
            "dfp",
            "dfp_service",
            "id",
            "name",
            "ophid",
            "protocol_absolute_name",
            "provider_id",
            "site_id",
            "type",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of associated_server
        if self.associated_server:
            _dict['associated_server'] = self.associated_server.to_dict()
        # override the default output from pydantic by calling `to_dict()` of inheritance_sources
        if self.inheritance_sources:
            _dict['inheritance_sources'] = self.inheritance_sources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in kerberos_keys (list)
        _items = []
        if self.kerberos_keys:
            for _item in self.kerberos_keys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['kerberos_keys'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Host from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "absolute_name":
            obj.get("absolute_name"),
            "address":
            obj.get("address"),
            "anycast_addresses":
            obj.get("anycast_addresses"),
            "associated_server":
            HostAssociatedServer.from_dict(obj["associated_server"])
            if obj.get("associated_server") is not None else None,
            "comment":
            obj.get("comment"),
            "current_version":
            obj.get("current_version"),
            "dfp":
            obj.get("dfp"),
            "dfp_service":
            obj.get("dfp_service"),
            "id":
            obj.get("id"),
            "inheritance_sources":
            HostInheritance.from_dict(obj["inheritance_sources"])
            if obj.get("inheritance_sources") is not None else None,
            "kerberos_keys":
            [KerberosKey.from_dict(_item) for _item in obj["kerberos_keys"]]
            if obj.get("kerberos_keys") is not None else None,
            "name":
            obj.get("name"),
            "ophid":
            obj.get("ophid"),
            "protocol_absolute_name":
            obj.get("protocol_absolute_name"),
            "provider_id":
            obj.get("provider_id"),
            "server":
            obj.get("server"),
            "site_id":
            obj.get("site_id"),
            "tags":
            obj.get("tags"),
            "type":
            obj.get("type")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
