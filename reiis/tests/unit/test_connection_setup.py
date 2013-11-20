"""Verify that the code for establishing connections to redis works as expected
and handles error conditions appropriately.

"""
from unittest.case import TestCase
from mock import patch

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

    
