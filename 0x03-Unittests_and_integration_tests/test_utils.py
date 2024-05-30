#!/usr/bin/env python3
"""Module for testing utils."""

from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
import requests


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Check method returns correct value."""

        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Check KeyError is raised with correct message."""

        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """Tests for get_json."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])


    def test_get_json(self, test_url, test_payload):
        """Check get_json returns correct payload."""

        cnfg = {'return_value.json.return_value': test_payload}
        patch = patch('requests.get', **cnfg)
        mock = patch.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patch.stop()


class TestMemoize(unittest.TestCase):
    """Tests for memoize."""

    def test_memoize(self):
        """Check memoize caches method results."""

        class TestClass:
            """Class to test memoize."""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            t_class = TestClass()
            t_class.a_property()
            t_class.a_property()
            mock.assert_called_once()
