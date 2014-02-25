"""In order to issue commands to redis we need to first establish a connection.
This module contains the interface for establishing connections to redis.

"""
from redis import StrictRedis


# The default port used for connections
DEFAULT_REDIS_PORT = 6397


def setup(host, port=DEFAULT_REDIS_PORT):
    """Establish a new connection to a redis server.

    In order to establish a connection to redis we need to know how to contact
    the server. This method should be called before using any of the data
    structures provided by reiis as it establish the connection to be used.

    Args:
        host: The IP address of the host server (basestring)
        port: The port to connect to (optional, default is 6379)
    """
    if not isinstance(host, basestring):
        raise TypeError("Expected basestring, found `{}'".format(repr(host)))
