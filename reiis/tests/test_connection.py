from mock import patch
import redis
from reiis import connection, exceptions
from unittest import TestCase


class BaseConnectionTestCase(TestCase):

    def tearDown(self):
        super(BaseConnectionTestCase, self).tearDown()
        connection.global_redis = None


class SetupTest(BaseConnectionTestCase):

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

    def test_should_attempt_to_initialize_redis_with_given_values(self):
        """Should attempt to initialize redis connection with given values"""
        with patch.object(redis.StrictRedis, '__init__', return_value=None) as redis_init:
            connection.setup('localhost', 1234)
        redis_init.assert_called_with(host='localhost', port=1234)


class ConnectionManagerTest(BaseConnectionTestCase):

    def test_should_raise_error_if_no_connection_establish(self):
        """Should raise connection error if no connection was established"""
        with self.assertRaises(exceptions.ConnectionError):
            with connection.connection_manager():
                pass

    def test_should_yield_value_of_global_redis(self):
        """Should yield the value of the global redis connection"""
        connection.global_redis = [1, 2]
        with connection.connection_manager() as conn:
            self.assertEquals(conn, [1, 2])
