"""For creating an Organization"""
from .base_api import BaseAPI


class Organization(BaseAPI):
    # A list of all arguments for a Organization
    keyword_arguments = [
        "address",
        "billing_id",
        "city",
        "company",
        "contact_fname",
        "contact_lname",
        "country",
        "crm_id",
        "custom_fields",
        "date_create",
        "date_edit",
        "dept",
        "email",
        "fax",
        "latitude",
        "logs",
        "longitude",
        "notes",
        "notification_append",
        "phone",
        "state",
        "theme",
        "title",
        "tollfree",
        "updated_by",
        "zip",
    ]

    uri = '/api/organization'

    @classmethod
    def find(cls, search_string, search_spec='company'):
        """Find an Organization based on its name"""
        return super().find(
            uri=cls.uri,
            search_spec=search_spec,
            search_string=search_string,
        )

    @classmethod
    def get_uri(cls, search_string, search_spec='company'):
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
    def create(cls, search_string, search_spec='company', **kwargs):
        """Creates an item on the server"""
        payload = cls.payload(search_spec=search_string, **kwargs)

        return super().create(
            uri=cls.uri,
            search_spec=search_spec,
            search_string=search_string,
            payload=payload
        )
