"""In order to issue commands to redis we need to first establish a connection.
This module contains the interface for establishing connections to redis. This
module is typically to be used to establish the initial connection to redis as
follows:

>>> import reiis
>>> reiis.setup('localhost', 1234)

"""
from contextlib import contextmanager
from reiis.exceptions import ConnectionError
import redis


# The default port used for connections
DEFAULT_REDIS_PORT = 6379

# The global instance of the redis connection (internally pools connections)
redis_connection = None


def setup(host, port=DEFAULT_REDIS_PORT):
    """Establish a new connection to a redis server.

    In order to establish a connection to redis we need to know how to contact
    the server. This method should be called before using any of the data
    structures provided by reiis as it establish the connection to be used.

    Args:
        host: The IP address of the host server (basestring)
        port: The port to connect to (optional, default is 6379)

    Raises:
        TypeError: One of the parameters was of an invalid type.
        redis.ConnectionError: If connection failed or pooling issue occurred.
    """
    global redis_connection
    
    if not isinstance(host, basestring):
        raise TypeError("Expected basestring, found `{}'".format(repr(host)))
    if not isinstance(port, (int, long)):
        raise TypeError("Expected (int, long), found `{}'".format(repr(port)))

    if not redis_connection:
        redis_connection = redis.StrictRedis(host=host, port=port)


@contextmanager
def connection_manager():
    """Retrieve global connection instance for use in code block.

    In order to make retrieving a connection and using it within a block of code
    effortless without having to constantly retrieve a connection by hand this
    context manager is provided as a convenience mechanism. It can be used as
    follows:

    >>> with reiis.connection_manager() as connection:
    >>>    connect.sadd('my-set', 1)

    Returns:
        A redis connection instance.

    Raises:
        ConnectionError: When no connection was established prior to use.
    """
    global redis_connection

    if not redis_connection:
        raise ConnectionError(
            'Attempted to use redis connection before establishing one')

    yield redis_connection
