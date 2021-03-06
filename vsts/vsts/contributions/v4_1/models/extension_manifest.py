# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ExtensionManifest(Model):
    """ExtensionManifest.

    :param base_uri: Uri used as base for other relative uri's defined in extension
    :type base_uri: str
    :param constraints: List of shared constraints defined by this extension
    :type constraints: list of :class:`ContributionConstraint <contributions.v4_1.models.ContributionConstraint>`
    :param contributions: List of contributions made by this extension
    :type contributions: list of :class:`Contribution <contributions.v4_1.models.Contribution>`
    :param contribution_types: List of contribution types defined by this extension
    :type contribution_types: list of :class:`ContributionType <contributions.v4_1.models.ContributionType>`
    :param demands: List of explicit demands required by this extension
    :type demands: list of str
    :param event_callbacks: Collection of endpoints that get called when particular extension events occur
    :type event_callbacks: :class:`ExtensionEventCallbackCollection <contributions.v4_1.models.ExtensionEventCallbackCollection>`
    :param fallback_base_uri: Secondary location that can be used as base for other relative uri's defined in extension
    :type fallback_base_uri: str
    :param language: Language Culture Name set by the Gallery
    :type language: str
    :param licensing: How this extension behaves with respect to licensing
    :type licensing: :class:`ExtensionLicensing <contributions.v4_1.models.ExtensionLicensing>`
    :param manifest_version: Version of the extension manifest format/content
    :type manifest_version: float
    :param restricted_to: Default user claims applied to all contributions (except the ones which have been speficied restrictedTo explicitly) to control the visibility of a contribution.
    :type restricted_to: list of str
    :param scopes: List of all oauth scopes required by this extension
    :type scopes: list of str
    :param service_instance_type: The ServiceInstanceType(Guid) of the VSTS service that must be available to an account in order for the extension to be installed
    :type service_instance_type: str
    """

    _attribute_map = {
        'base_uri': {'key': 'baseUri', 'type': 'str'},
        'constraints': {'key': 'constraints', 'type': '[ContributionConstraint]'},
        'contributions': {'key': 'contributions', 'type': '[Contribution]'},
        'contribution_types': {'key': 'contributionTypes', 'type': '[ContributionType]'},
        'demands': {'key': 'demands', 'type': '[str]'},
        'event_callbacks': {'key': 'eventCallbacks', 'type': 'ExtensionEventCallbackCollection'},
        'fallback_base_uri': {'key': 'fallbackBaseUri', 'type': 'str'},
        'language': {'key': 'language', 'type': 'str'},
        'licensing': {'key': 'licensing', 'type': 'ExtensionLicensing'},
        'manifest_version': {'key': 'manifestVersion', 'type': 'float'},
        'restricted_to': {'key': 'restrictedTo', 'type': '[str]'},
        'scopes': {'key': 'scopes', 'type': '[str]'},
        'service_instance_type': {'key': 'serviceInstanceType', 'type': 'str'}
    }

    def __init__(self, base_uri=None, constraints=None, contributions=None, contribution_types=None, demands=None, event_callbacks=None, fallback_base_uri=None, language=None, licensing=None, manifest_version=None, restricted_to=None, scopes=None, service_instance_type=None):
        super(ExtensionManifest, self).__init__()
        self.base_uri = base_uri
        self.constraints = constraints
        self.contributions = contributions
        self.contribution_types = contribution_types
        self.demands = demands
        self.event_callbacks = event_callbacks
        self.fallback_base_uri = fallback_base_uri
        self.language = language
        self.licensing = licensing
        self.manifest_version = manifest_version
        self.restricted_to = restricted_to
        self.scopes = scopes
        self.service_instance_type = service_instance_type
