"""Verify that the module for establishing connections to redis works as
expected and handles error conditions appropriately.

"""
from unittest.case import TestCase
from mock import patch
import redis

from reiis import connection


def test_should_raise_exception_if_none_value_given_for_host():
    """Should raise TypeError if None value given for host"""
    connection.setup.when.called_with(None).should.throw(
        TypeError, 'Expected host to be basestring, found None')
        

def test_should_raise_exception_if_non_string_object_given_for_port():
    """Should raise TypeError if non-string object given host"""
    connection.setup.when.called_with([1, 2]).should.throw(
        TypeError, 'Expected host to be basestring, found [1, 2]')


def test_should_raise_exception_if_none_value_given_for_port():
    """Should raise TypeError if None value given for port"""
    connection.setup.when.called_with('localhost', None).should.throw(
        TypeError, 'Expected port to be (int, long), found None')

    
def test_should_raise_exception_if_non_int_value_given_for_port():
    """Should raise TypeError if None value given for port"""
    connection.setup.when.called_with('localhost', [1, 2]).should.throw(
        TypeError, 'Expected port to be (int, long), found [1, 2]')

    
def test_should_pass_parameters_to_redis_on_success():
    """Should pass the host and port to redis on success"""
    with patch.object(redis.Redis, '__init__', return_value=None) as init_redis:
        connection.setup('localhost', 1234)
    init_redis.assert_called_with('localhost', 1234)
