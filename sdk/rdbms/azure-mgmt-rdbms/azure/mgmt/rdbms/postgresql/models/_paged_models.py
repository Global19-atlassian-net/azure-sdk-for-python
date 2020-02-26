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

from msrest.paging import Paged


class ServerPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Server <azure.mgmt.rdbms.postgresql.models.Server>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Server]'}
    }

    def __init__(self, *args, **kwargs):

        super(ServerPaged, self).__init__(*args, **kwargs)
class FirewallRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`FirewallRule <azure.mgmt.rdbms.postgresql.models.FirewallRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[FirewallRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(FirewallRulePaged, self).__init__(*args, **kwargs)
class VirtualNetworkRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualNetworkRule <azure.mgmt.rdbms.postgresql.models.VirtualNetworkRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualNetworkRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualNetworkRulePaged, self).__init__(*args, **kwargs)
class DatabasePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Database <azure.mgmt.rdbms.postgresql.models.Database>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Database]'}
    }

    def __init__(self, *args, **kwargs):

        super(DatabasePaged, self).__init__(*args, **kwargs)
class ConfigurationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Configuration <azure.mgmt.rdbms.postgresql.models.Configuration>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Configuration]'}
    }

    def __init__(self, *args, **kwargs):

        super(ConfigurationPaged, self).__init__(*args, **kwargs)
class LogFilePaged(Paged):
    """
    A paging container for iterating over a list of :class:`LogFile <azure.mgmt.rdbms.postgresql.models.LogFile>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[LogFile]'}
    }

    def __init__(self, *args, **kwargs):

        super(LogFilePaged, self).__init__(*args, **kwargs)
class PerformanceTierPropertiesPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PerformanceTierProperties <azure.mgmt.rdbms.postgresql.models.PerformanceTierProperties>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PerformanceTierProperties]'}
    }

    def __init__(self, *args, **kwargs):

        super(PerformanceTierPropertiesPaged, self).__init__(*args, **kwargs)
class PrivateEndpointConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateEndpointConnection <azure.mgmt.rdbms.postgresql.models.PrivateEndpointConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateEndpointConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateEndpointConnectionPaged, self).__init__(*args, **kwargs)
class PrivateLinkResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateLinkResource <azure.mgmt.rdbms.postgresql.models.PrivateLinkResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateLinkResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateLinkResourcePaged, self).__init__(*args, **kwargs)