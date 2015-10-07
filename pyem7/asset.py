"""For dealing with Assets"""
from .base_api import BaseAPI


class Asset(BaseAPI):
    # A list of all arguments for a asset
    keyword_arguments = [
        "asset_tag",
        "components",
        "configuration",
        "date_edit",
        "device",
        "edited_by",
        "floor",
        "function",
        "licenses",
        "location",
        "location_notes",
        "maintenance",
        "make",
        "model",
        "networks",
        "organization",
        "owner",
        "owner_admin",
        "owner_tech",
        "panel",
        "plate",
        "punch",
        "rack",
        "rfid",
        "room",
        "serial",
        "shelf",
        "status",
        "type",
        "vital_notes",
        "zone",
    ]

    uri = '/api/asset'
    dicts = ['components', 'configuration', 'licenses', 'maintenance', 'networks']

    @classmethod
    def find(cls, uri='/api/asset', search_spec='organization',
             search_string='test_asset'):
        """Find an asset based on its name"""
        return super().find(uri=uri, search_spec=search_spec,
                            search_string=search_string)

    @classmethod
    def get_uri(cls, search_string, search_spec='organization'):
        """Get the URI for an item

            :param organization: The name of the organization you need the URI for

            :return: returns servers response to the GET request
        """
        return super().get_uri(
            uri=cls.uri,
            search_spec=search_spec,
            search_string=search_string,
            extended_fetch=False
        )

    @classmethod
    def create(cls, search_string, search_spec='organization', **kwargs):
        """Creates an item on the server"""
        payload = cls.payload(search_spec=search_string, **kwargs)

        return super().create(
            uri=cls.uri,
            search_spec=search_spec,
            search_string=search_string,
            payload=payload
        )
