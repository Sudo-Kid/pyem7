"""Will need to update payload later to remove ip_address"""
from urllib.parse import urljoin

from .base_api import BaseAPI
from .custom_errors import Exists


class Discovery(BaseAPI):
    # A list of all arguments for a Discovery
    keyword_arguments = [
        "aligned_collector",
        "aligned_device_template",
        "credentials",
        "date_edit",
        "date_run",
        "description",
        "device_groups",
        "dhcp_enabled",
        "discover_non_snmp",
        "duplicate_protection",
        "edited_by",
        "hostnames",
        "initial_scan_level",
        "ip_lists",
        "log_all",
        "logs",
        "model_device",
        "name",
        "organization",
        "port_scan_timeout",
        "scan_all_ips",
        "scan_ports",
        "scan_throttle",
    ]

    uri = '/api/discovery_session'
    uri_active = '/api/discovery_session_active'

    lists = [
        'ip_lists', 'credentials', 'hostnames', 'scan_ports', 'device_groups'
    ]

    bools = ['initial_scan_level', 'port_scan_timeout', 'scan_throttle']
    dicts = ['logs']

    @classmethod
    def create(cls, search_spec, search_string, payload):
        """Creates a discovery on the server"""

        exists = cls.find(uri='/api/device', search_spec=search_spec,
                          search_string=search_string, extended_fetch=False)

        if not exists.json():
            return cls.post(cls.uri_active, payload)
        else:
            return exists

    @classmethod
    def check(cls, uri):
        uri = urljoin(uri, '?hide_filterinfo=1')
        return super().get(uri)

    @classmethod
    def find(cls, uri='/api/discovery_session', search_spec='description',
             search_string='test_server', extended_fetch=False):
        return super().find(uri=uri, search_spec=search_spec,
                            search_string=search_string, extended_fetch=extended_fetch)
