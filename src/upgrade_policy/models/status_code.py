# coding: utf-8

"""
    Schedule Software/Config Updates

    Infoblox by default does automatic software updates when they become available. Updates are applied to all on-prem hosts, physical or virtual. However, you can override and schedule the software updates. You can also defer the updates to a later date and time. You can configure up to a total of 50 deferrals (scheduled and deferred software updates), which means you have the flexibility to create up to 50 update groups across different on-prem hosts by mapping with appropriate tags. Tags are be used to associate deferrals (scheduled or deferred) with a specific or group of onprem-hosts. Apart from software update deferrals, config update deferrals also can be configured using these overrides.

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class StatusCode(str, Enum):
    """
    StatusCode
    """
    """
    allowed enum values
    """
    SUCCESS = 'SUCCESS'
    GENERAL_FAILURE = 'GENERAL_FAILURE'
    HASH_FAILURE = 'HASH_FAILURE'
    VALIDATION_FAILURE = 'VALIDATION_FAILURE'
    COPY_FAILURE = 'COPY_FAILURE'
    RELOAD_FAILIURE = 'RELOAD_FAILIURE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StatusCode from a JSON string"""
        return cls(json.loads(json_str))
