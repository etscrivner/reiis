"""In order to properly encapsulate errors specfic to this library itself we
provide a unified set of exceptions descended from a common base class. For
example, if you'd like to catch all errors originating from this module:

>>> try:
>>>    # Some reiis stuff
>>> except reiis.Error:
>>>    pass

"""

class Error(Exception):
    """Base class for all exceptions within this package to make catching all
    exceptions from this package a possibility.

    """
    pass


class ConnectionError(Exception):
    """Represents an error that has occurred while trying to establish a connection
    to redis and which did not originate from within the redis package.

    """
    pass
