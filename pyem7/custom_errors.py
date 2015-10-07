class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class KeywordArgument(Error):
    pass


class AuthError(Error):
    pass


class MultipleRecordsFound(Error):
    pass


class Exists(Error):
    pass
