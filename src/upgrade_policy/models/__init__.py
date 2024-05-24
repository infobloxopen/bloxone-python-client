# coding: utf-8

# flake8: noqa
"""
    Schedule Software/Config Updates

    Infoblox by default does automatic software updates when they become available. Updates are applied to all on-prem hosts, physical or virtual. However, you can override and schedule the software updates. You can also defer the updates to a later date and time. You can configure up to a total of 50 deferrals (scheduled and deferred software updates), which means you have the flexibility to create up to 50 update groups across different on-prem hosts by mapping with appropriate tags. Tags are be used to associate deferrals (scheduled or deferred) with a specific or group of onprem-hosts. Apart from software update deferrals, config update deferrals also can be configured using these overrides.

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

# import models into model package
from upgrade_policy.models.apply_config_now_request import ApplyConfigNowRequest
from upgrade_policy.models.apply_config_now_response import ApplyConfigNowResponse
from upgrade_policy.models.apply_config_now_status import ApplyConfigNowStatus
from upgrade_policy.models.batch_maintenance_window import BatchMaintenanceWindow
from upgrade_policy.models.batch_maintenance_window_request import BatchMaintenanceWindowRequest
from upgrade_policy.models.batch_maintenance_window_response import BatchMaintenanceWindowResponse
from upgrade_policy.models.batch_maintenance_window_result import BatchMaintenanceWindowResult
from upgrade_policy.models.create_maintenance_window import CreateMaintenanceWindow
from upgrade_policy.models.create_maintenance_window_request import CreateMaintenanceWindowRequest
from upgrade_policy.models.create_maintenance_window_response import CreateMaintenanceWindowResponse
from upgrade_policy.models.deferred_window import DeferredWindow
from upgrade_policy.models.delete_maintenance_window_response import DeleteMaintenanceWindowResponse
from upgrade_policy.models.get_maintenance_window_response import GetMaintenanceWindowResponse
from upgrade_policy.models.list_maintenance_window_response import ListMaintenanceWindowResponse
from upgrade_policy.models.maintenance_window import MaintenanceWindow
from upgrade_policy.models.onprem_details import OnpremDetails
from upgrade_policy.models.scheduled_window import ScheduledWindow
from upgrade_policy.models.status_code import StatusCode
from upgrade_policy.models.update_batch_maintenance_window import UpdateBatchMaintenanceWindow
from upgrade_policy.models.update_maintenance_window import UpdateMaintenanceWindow
from upgrade_policy.models.update_maintenance_window_request import UpdateMaintenanceWindowRequest
from upgrade_policy.models.update_maintenance_window_response import UpdateMaintenanceWindowResponse
