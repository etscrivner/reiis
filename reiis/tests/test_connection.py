from unittest import TestCase
from reiis import connection


class SetupTest(TestCase):

    def test_should_raise_type_error_if_none_given_for_host(self):
        """Should raise TypeError if None given for `host' argument"""
        with self.assertRaises(TypeError):
            connection.setup(None)

    def test_should_raise_type_error_if_non_string_value_given_for_host(self):
        """Should raise TypeError if non-basestring value given for `host' argument"""
        with self.assertRaises(TypeError):
            connection.setup([1, 2])
        
