"""Verify that the code for establishing connections to redis works as expected
and handles error conditions appropriately.

"""
from unittest.case import TestCase
from mock import patch

from reiis import connection


def test_should_raise_exception_if_none_value_given():
    """Should raise TypeError if None value given"""
    connection.setup.when.called_with(None).should.throw(
        TypeError, 'Expected tuple, found None')
        

def test_should_raise_exception_if_non_tuple_object_given():
    """Should raise TypeError if non-tuple object given"""
    connection.setup.when.called_with([1, 2]).should.throw(
        TypeError, 'Expected tuple, found [1, 2]')
