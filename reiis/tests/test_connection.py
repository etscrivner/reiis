from mock import patch
import redis
from reiis import connection
from unittest import TestCase


class SetupTest(TestCase):

    def test_should_raise_type_error_if_none_given_for_host(self):
        """Should raise TypeError if None given for `host' argument"""
        with self.assertRaises(TypeError):
            connection.setup(None)

    def test_should_raise_type_error_if_non_string_value_given_for_host(self):
        """Should raise TypeError if non-basestring value given for `host' argument"""
        with self.assertRaises(TypeError):
            connection.setup([1, 2])

    def test_should_raise_type_error_if_port_is_none_value(self):
        """Should raise TypeError if None given for `port' argument"""
        with self.assertRaises(TypeError):
            connection.setup('localhost', None)

    def test_should_raise_type_error_if_port_is_non_integral_value(self):
        """Should raise TypeError if non-integer given for `port' argument"""
        with self.assertRaises(TypeError):
            connection.setup('localhost', [1, 2])
    
    def test_should_raise_redis_connection_error_if_connection_fails(self):
        """Should raise redis.ConnectionError if connection fails"""
        with self.assertRaises(redis.ConnectionError):
            with patch.object(redis.StrictRedis, '__init__') as redis_init:
                redis_init.side_effect = redis.ConnectionError('bad')
                connection.setup('localhost')
