"""In order to query redis we need to first establish a connection to be used 
across all of our objects. This module contains the interface for establishing
the connection and handle connection specific errors that may arise.

"""
from collections import namedtuple

import redis


# The default port used for redis connections without a given port
REDIS_DEFAULT_PORT = 6379


# Defines a redis host for establishing a connection
Host = namedtuple('Host', ['address', 'port'])


def setup(host, port=REDIS_DEFAULT_PORT):
    """Attempt to establish a connection to redis.

    This method will attempt to establish a redis connection using the given
    host and port. If connecting fails then an exception may be raised from
    the underlying redis library.

    :Parameters:

      - `host` basestring - The connection host address
      - `port` int (optional) - The port to connect to

    :Examples:

    >>> from reiis import connection
    >>> connection.setup('localhost', 6379)
    >>> connection.setup('localhost')

    """
    if not isinstance(host, basestring):
        raise TypeError(
            'Expected host to be basestring, found {}'.format(repr(host)))
    if not isinstance(port, (int, long)):
        raise TypeError(
            'Expected port to be (int, long), found {}'.format(repr(port)))
    
