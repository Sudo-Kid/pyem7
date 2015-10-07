from .base_api import BaseAPI
from .discovery import Discovery


class Device(BaseAPI):
    # A list of all arguments for a device
    keyword_arguments = [
        "active",
        "alert_avail_and_latency_fail",
        "app_credentials",
        "applications",
        "auto_clear"
        "auto_update"
        "child_devices"
        "class_type"
        "collector_group"
        "config_data"
        "critical_ping"
        "daily_port_scan"
        "dashboard"
        "date_added"
        "details"
        "disable_asset_update"
        "event_suppress_mask"
        "hostname"
        "interfaces"
        "ip"
        "l3_topo"
        "last_poll"
        "log_all"
        "logs"
        "name"
        "notes"
        "organization"
        "parent_device"
        "performance_data"
        "preserve_hostname"
        "scan_all_ips"
        "snmp_cred_id"
        "snmp_w_cred_id"
        "state"
        "thresholds",
        "vitals"
    ]

    uri = '/api/device'

    @classmethod
    def find(cls, uri='/api/device', search_spec='ip', search_string='test',
             extended_fetch=False):
        return super().find(uri=uri, search_spec=search_spec,
                            search_string=search_string, extended_fetch=extended_fetch)

    @classmethod
    def get_uri(cls, search_string, search_spec='ip'):
        """Get the URI for an item

            :param company: The name of the company you need the URI for

            :return: returns servers response to the GET request
        """
        return super().get_uri(
            uri=cls.uri,
            search_spec=search_spec,
            search_string=search_string
        )

    @classmethod
    def create(cls, aligned_device_template, description, search_spec='description',
               **kwargs):
        """Creates a device on the API server

            :param:

            :return:
        """
        return Discovery.create(
            aligned_device_template,
            description,
            search_spec='description',
            **kwargs)
