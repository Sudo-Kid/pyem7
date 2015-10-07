"""For creating an Organization"""
from pyem7.base_api import BaseAPI


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
    def create(cls, search_spec, search_string, payload):
        return super().create(uri=cls.uri, search_spec=search_spec,
                              search_string=search_string, payload=payload)

    @classmethod
    def find(cls, uri='/api/organization', search_spec='company',
             search_string='test_server', extended_fetch=False):
        return super().find(uri=uri, search_spec=search_spec,
                            search_string=search_string)
