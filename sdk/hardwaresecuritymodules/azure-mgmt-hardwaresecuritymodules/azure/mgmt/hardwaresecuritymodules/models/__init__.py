# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ApiEntityReference
from ._models_py3 import BackupRequestProperties
from ._models_py3 import BackupRestoreBaseResultProperties
from ._models_py3 import BackupRestoreRequestBaseProperties
from ._models_py3 import BackupResult
from ._models_py3 import BackupResultProperties
from ._models_py3 import CloudHsmCluster
from ._models_py3 import CloudHsmClusterListResult
from ._models_py3 import CloudHsmClusterPatchParameters
from ._models_py3 import CloudHsmClusterProperties
from ._models_py3 import CloudHsmClusterResource
from ._models_py3 import CloudHsmClusterSku
from ._models_py3 import CloudHsmProperties
from ._models_py3 import DedicatedHsm
from ._models_py3 import DedicatedHsmError
from ._models_py3 import DedicatedHsmListResult
from ._models_py3 import DedicatedHsmPatchParameters
from ._models_py3 import DedicatedHsmProperties
from ._models_py3 import EndpointDependency
from ._models_py3 import EndpointDetail
from ._models_py3 import Error
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import ManagedServiceIdentity
from ._models_py3 import NetworkInterface
from ._models_py3 import NetworkProfile
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import OutboundEnvironmentEndpoint
from ._models_py3 import OutboundEnvironmentEndpointCollection
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateEndpointConnectionProperties
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkResourceProperties
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import ProxyResource
from ._models_py3 import Resource
from ._models_py3 import RestoreRequestProperties
from ._models_py3 import RestoreResult
from ._models_py3 import Sku
from ._models_py3 import SystemData
from ._models_py3 import TrackedResource
from ._models_py3 import UserAssignedIdentity

from ._hardware_security_modules_mgmt_client_enums import ActionType
from ._hardware_security_modules_mgmt_client_enums import ActivationState
from ._hardware_security_modules_mgmt_client_enums import AutoGeneratedDomainNameLabelScope
from ._hardware_security_modules_mgmt_client_enums import BackupRestoreOperationStatus
from ._hardware_security_modules_mgmt_client_enums import CloudHsmClusterSkuFamily
from ._hardware_security_modules_mgmt_client_enums import CloudHsmClusterSkuName
from ._hardware_security_modules_mgmt_client_enums import CreatedByType
from ._hardware_security_modules_mgmt_client_enums import IdentityType
from ._hardware_security_modules_mgmt_client_enums import JsonWebKeyType
from ._hardware_security_modules_mgmt_client_enums import ManagedServiceIdentityType
from ._hardware_security_modules_mgmt_client_enums import Origin
from ._hardware_security_modules_mgmt_client_enums import PrivateEndpointConnectionProvisioningState
from ._hardware_security_modules_mgmt_client_enums import PrivateEndpointServiceConnectionStatus
from ._hardware_security_modules_mgmt_client_enums import ProvisioningState
from ._hardware_security_modules_mgmt_client_enums import PublicNetworkAccess
from ._hardware_security_modules_mgmt_client_enums import SkuName
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ApiEntityReference",
    "BackupRequestProperties",
    "BackupRestoreBaseResultProperties",
    "BackupRestoreRequestBaseProperties",
    "BackupResult",
    "BackupResultProperties",
    "CloudHsmCluster",
    "CloudHsmClusterListResult",
    "CloudHsmClusterPatchParameters",
    "CloudHsmClusterProperties",
    "CloudHsmClusterResource",
    "CloudHsmClusterSku",
    "CloudHsmProperties",
    "DedicatedHsm",
    "DedicatedHsmError",
    "DedicatedHsmListResult",
    "DedicatedHsmPatchParameters",
    "DedicatedHsmProperties",
    "EndpointDependency",
    "EndpointDetail",
    "Error",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "ManagedServiceIdentity",
    "NetworkInterface",
    "NetworkProfile",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "OutboundEnvironmentEndpoint",
    "OutboundEnvironmentEndpointCollection",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionListResult",
    "PrivateEndpointConnectionProperties",
    "PrivateLinkResource",
    "PrivateLinkResourceListResult",
    "PrivateLinkResourceProperties",
    "PrivateLinkServiceConnectionState",
    "ProxyResource",
    "Resource",
    "RestoreRequestProperties",
    "RestoreResult",
    "Sku",
    "SystemData",
    "TrackedResource",
    "UserAssignedIdentity",
    "ActionType",
    "ActivationState",
    "AutoGeneratedDomainNameLabelScope",
    "BackupRestoreOperationStatus",
    "CloudHsmClusterSkuFamily",
    "CloudHsmClusterSkuName",
    "CreatedByType",
    "IdentityType",
    "JsonWebKeyType",
    "ManagedServiceIdentityType",
    "Origin",
    "PrivateEndpointConnectionProvisioningState",
    "PrivateEndpointServiceConnectionStatus",
    "ProvisioningState",
    "PublicNetworkAccess",
    "SkuName",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
