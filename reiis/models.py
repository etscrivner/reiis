"""This file contains the objects representing the various data structures
in redis.

"""
from reiis.connection import get_connection


class BaseRedisDataStructure(object):
    """In order to avoid redundancy and at the same time maintain a consistent
    and generalized interface this class encapsulates shared similarities
    between all redis data-structures.

    """

    def __init__(self, key):
        """Initialize this data structure.

        Initializes this redis data structure interface with the given
        information.

        :Parameters:

          - `key` - basestring - The redis key

        """
        self.key = key

    @classmethod
    def get(cls, key, greedy=False):
        """Retrieve an instance of a data-structure from the given key.
        
        In sub-classes this method will be used to retrieve an instance of an
        object from its redis key.

        If the base class method is called then a NotImplementedError exception
        is raised.

        :Parameters:

          - `key` basestring - The redis key
          - `greedy` bool - If true, all available data will be loaded out on
            object initialization. Otherwise, it will be loaded on first
            access.

        :Returns:
          An instance of the given data structure linked to the key

        :Return Type:
          BaseRedisDataStructure
        
        """
        raise NotImplementedError
