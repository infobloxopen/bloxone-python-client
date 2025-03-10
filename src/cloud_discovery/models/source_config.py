# coding: utf-8

"""
    Discovery Configuration API V2

    The Discovery configuration service is a Universal DDI Service that provides configuration for accessing and syncing the Cloud assets   Base Paths:  1. provider: **/api/cloud_discovery/v2/**  

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cloud_discovery.models.account import Account
from cloud_discovery.models.credential_config import CredentialConfig
from typing import Optional, Set
from typing_extensions import Self


class SourceConfig(BaseModel):
    """
    Source configuration
    """

  # noqa: E501
    account_schedule_id: Optional[StrictStr] = Field(
        default=None, description="Account Schedule ID.")
    accounts: Optional[List[Account]] = None
    cloud_credential_id: Optional[StrictStr] = Field(
        default=None, description="Cloud Credential ID.")
    created_at: Optional[datetime] = Field(
        default=None,
        description="Timestamp when the object has been created.")
    credential_config: Optional[CredentialConfig] = Field(
        default=None,
        description=
        "Credential configuration. Ex.: '{    \"access_identifier\": \"arn:aws:iam::1234:role/access_for_discovery\",    \"region\": \"us-east-1\",    \"enclave\": \"commercial/gov\"  }'."
    )
    deleted_at: Optional[datetime] = Field(
        default=None,
        description="Timestamp when the object has been deleted.")
    id: Optional[StrictStr] = Field(
        default=None,
        description="Auto-generated unique source config ID. Format BloxID.")
    restricted_to_accounts: Optional[List[StrictStr]] = Field(
        default=None,
        description=
        "Provider account IDs such as accountID/ SubscriptionID to be restricted for a given source_config."
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        description="Timestamp when the object has been updated.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "account_schedule_id", "accounts", "cloud_credential_id", "created_at",
        "credential_config", "deleted_at", "id", "restricted_to_accounts",
        "updated_at"
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
        """Create an instance of SourceConfig from a JSON string"""
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
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "account_schedule_id",
            "created_at",
            "deleted_at",
            "updated_at",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in accounts (list)
        _items = []
        if self.accounts:
            for _item in self.accounts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accounts'] = _items
        # override the default output from pydantic by calling `to_dict()` of credential_config
        if self.credential_config:
            _dict['credential_config'] = self.credential_config.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SourceConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account_schedule_id":
            obj.get("account_schedule_id"),
            "accounts":
            [Account.from_dict(_item) for _item in obj["accounts"]]
            if obj.get("accounts") is not None else None,
            "cloud_credential_id":
            obj.get("cloud_credential_id"),
            "created_at":
            obj.get("created_at"),
            "credential_config":
            CredentialConfig.from_dict(obj["credential_config"])
            if obj.get("credential_config") is not None else None,
            "deleted_at":
            obj.get("deleted_at"),
            "id":
            obj.get("id"),
            "restricted_to_accounts":
            obj.get("restricted_to_accounts"),
            "updated_at":
            obj.get("updated_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
