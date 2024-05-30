#!/usr/bin/env python3
"""Module for testing the GithubOrgClient."""

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient."""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])

    @patch('client.get_json')
    def test_org(self, input, mock_get_json):

        """Ensure it returns the correct value."""
        t_client = GithubOrgClient(input)
        t_client.org()
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{input}')

    def test_public_repos_url(self):
        """Ensure it returns the correct URL."""

        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            payl = {"repos_url": "World"}
            mock_org.return_value = payl
            t_client = GithubOrgClient('test')
            res = t_client._public_repos_url
            self.assertEqual(res, payl["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Ensure that it returns the correct list of repos."""

        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_get_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "hello/world"
            t_client = GithubOrgClient('test')
            res = t_client.public_repos()
            exp = [repo["name"] for repo in json_payload]
            self.assertEqual(res, exp)
            mock_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test: has_license method."""
        res = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(res, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient (fixtures)."""

    @classmethod
    def setUpClass(cls):
        """Set up mock for requests.get."""

        cnfg = {'return_value.json.side_effect': [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload
        ]}
        cls.get_patcher = patch('requests.get', **cnfg)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """Test public repos."""

        t_client = GithubOrgClient("google")
        self.assertEqual(t_client.org, self.org_payload)
        self.assertEqual(t_client.repos_payload, self.repos_payload)
        self.assertEqual(t_client.public_repos(), self.expected_repos)
        self.assertEqual(t_client.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """Test public repos with license filtering."""

        t_client = GithubOrgClient("google")
        self.assertEqual(t_client.public_repos(), self.expected_repos)
        self.assertEqual(t_client.public_repos("XLICENSE"), [])
        self.assertEqual(t_client.public_repos("apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """Stop patcher for requests.get."""

        cls.get_patcher.stop()
