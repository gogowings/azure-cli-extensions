# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .tracked_resource import TrackedResource


class Workspace(TrackedResource):
    """Information about workspace.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :param managed_resource_group_id: Required. The managed resource group Id.
    :type managed_resource_group_id: str
    :param parameters: Name and value pairs that define the workspace
     parameters.
    :type parameters: object
    :ivar provisioning_state: The workspace provisioning state. Possible
     values include: 'Accepted', 'Running', 'Ready', 'Creating', 'Created',
     'Deleting', 'Deleted', 'Canceled', 'Failed', 'Succeeded', 'Updating'
    :vartype provisioning_state: str or
     ~azure.mgmt.databricks.models.ProvisioningState
    :param ui_definition_uri: The blob URI where the UI definition file is
     located.
    :type ui_definition_uri: str
    :param authorizations: The workspace provider authorizations.
    :type authorizations:
     list[~azure.mgmt.databricks.models.WorkspaceProviderAuthorization]
    :param sku: The SKU of the resource.
    :type sku: ~azure.mgmt.databricks.models.Sku
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'managed_resource_group_id': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'managed_resource_group_id': {'key': 'properties.managedResourceGroupId', 'type': 'str'},
        'parameters': {'key': 'properties.parameters', 'type': 'object'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'ui_definition_uri': {'key': 'properties.uiDefinitionUri', 'type': 'str'},
        'authorizations': {'key': 'properties.authorizations', 'type': '[WorkspaceProviderAuthorization]'},
        'sku': {'key': 'sku', 'type': 'Sku'},
    }

    def __init__(self, **kwargs):
        super(Workspace, self).__init__(**kwargs)
        self.managed_resource_group_id = kwargs.get('managed_resource_group_id', None)
        self.parameters = kwargs.get('parameters', None)
        self.provisioning_state = None
        self.ui_definition_uri = kwargs.get('ui_definition_uri', None)
        self.authorizations = kwargs.get('authorizations', None)
        self.sku = kwargs.get('sku', None)
