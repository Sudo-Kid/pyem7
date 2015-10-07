from pyem7.base_api import BaseAPI


class Account(BaseAPI):
    # A list of all arguments for a Account
    keyword_arguments = [
        "access_hooks",
        "active",
        "address",
        "admin",
        "aligned_organizations",
        "aligned_ticket_queues",
        "all_orgs",
        "autodetect_timezone",
        "barred",
        "billing_id",
        "cell",
        "city",
        "codehighlight",
        "console_height",
        "contact_fname",
        "contact_lname",
        "country",
        "create_date",
        "created_by",
        "critical",
        "crm_id",
        "date_format",
        "default_map",
        "default_map_type",
        "dept",
        "dev_html5_graph",
        "edit_date",
        "email",
        "email_2",
        "email_3",
        "event_severity",
        "events_default_view",
        "fax",
        "if_graph_perc",
        "iflabel_pref",
        "im",
        "im_type",
        "ldap",
        "login_state",
        "notes",
        "office",
        "organization",
        "page_results",
        "pager",
        "passwd",
        "passwd_expiration",
        "passwd_prev_count",
        "passwd_reset_required",
        "passwd_set_date",
        "passwd_strength",
        "permission_keys",
        "phone",
        "recent_timezone",
        "refresh",
        "restrict_ip",
        "role",
        "show_severity_badges",
        "state",
        "table_row_height",
        "theme",
        "ticket_note_sort",
        "timezone",
        "title",
        "tollfree",
        "updated_by",
        "user",
        "user_policy",
        "verification_answer",
        "verification_question",
        "zip"
    ]

    uri = '/api/account'

    dicts = ['access_hooks']
    bools = ['passwd_set_date']
    lists = ['aligned_organizations', 'aligned_ticket_queues', 'permission_keys']

    @classmethod
    def get_uri(cls, search_string, search_spec='user'):
        """Get the URI for an item

            :param user: The name of the user you need the URI for

            :return: returns servers response to the GET request
        """
        return super().get_uri(
            uri=cls.uri,
            search_spec=search_spec,
            search_string=search_string)

    @classmethod
    def create(cls, search_spec, search_string, payload):
        return super().create(uri=cls.uri, search_spec=search_spec,
                              search_string=search_string, payload=payload)

    @classmethod
    def find(cls, uri='/api/account', search_spec='', search_string='user',
             extended_fetch=False):
        return super().find(uri=uri, search_spec=search_spec,
                            search_string=search_string, extended_fetch=extended_fetch)
