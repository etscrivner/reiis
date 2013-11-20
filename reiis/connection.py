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


def setup(host_and_port):
    """Attempt to establish a connection to redis.

    This method will attempt to establish a redis connection using the given
    host and port. If connecting fails then an exception may be raised from
    the underlying redis library.

    :Parameters:

      - `host_and_port` tuple of (basestring) or (basestring, int) - The host or
        host and port.

    :Examples:

    >>> from reiis import connection
    >>> connection.setup(('localhost', 6379))
    >>> connection.setup(('localhost'))

    """
    if not isinstance(host_and_port, tuple):
        raise TypeError('Expected tuple, found {}'.format(repr(host_and_port)))
