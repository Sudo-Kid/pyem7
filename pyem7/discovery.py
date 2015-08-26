"""Will need to update payload later to remove ip_address"""
from urllib.parse import urljoin

from .base_api import BaseAPI


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
    def find(cls, search_string='test', search_spec='description'):
        """Find discovery based on name"""
        return super().find(
            uri=cls.uri,
            search_spec=search_spec,
            search_string=search_string
        )

    @classmethod
    def get_uri(cls, search_string, search_spec='name'):
        """Get the URI for an item

            :param company: The name of the company you need the URI for

            :return: returns servers response to the GET request
        """
        return super().get_uri(
            uri=cls.uri,
            search_spec=search_string,
            search_string=search_string
        )

    @classmethod
    def create(
        cls,
        aligned_device_template,
        description,
        search_spec='description',
        **kwargs
    ):
        """Creates a discovery on the server"""
        payload = cls.payload(
            aligned_device_template=aligned_device_template,
            description=description,
            **kwargs
        )

        return super().create(
            uri=cls.uri_active,
            search_spec=search_spec,
            search_string=description,
            payload=payload
        )

    @classmethod
    def check(cls, uri):
        uri = urljoin(uri, 'log?hide_filterinfo=1')
        return super().get(uri)
