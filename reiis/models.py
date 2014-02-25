"""This module provides reified versions of redis objects descended from their
native python equivalents.

"""
from reiis.connection import connection_manager


class List(list):
    """Front-end for accessing redis list as if it were a native python list and
    committing results back into redis.

    """

    def __init__(self, initial_value, key, force_type=False, **kwargs):
        """Initializes this redis list with a given value and assigns it the
        given key.

        Args:
            initial_value: The initial value for the list.
            key: The redis key to persist data into.
            force_type: A type to force values in array to as they all come
                back from redis as strings. Optional, an does no type coercion
                by default.
        """
        super(List, self).__init__(initial_value, **kwargs)
        self.key = key
        with connection_manager() as conn:
            if force_type is not None:
                self += [force_type(val) for val in conn.lrange(self.key, 0, -1)]
            else:
                self += conn.lrange(self.key, 0, -1)

    def commit(self):
        """Commits internal values into redis key using lpush.
        
        """
        with connection_manager() as conn:
            conn.lpush(self.key, *self)
